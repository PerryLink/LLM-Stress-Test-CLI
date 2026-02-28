"""核心压测引擎"""

import asyncio
import time
import json
from dataclasses import dataclass
from typing import List, Optional
import aiohttp
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from llm_stress_test_cli.utils import calculate_percentile, format_latency, calculate_success_rate


@dataclass
class RequestMetrics:
    """单次请求指标"""
    ttft: float = 0.0
    total_latency: float = 0.0
    tokens_generated: int = 0
    success: bool = False
    error: Optional[str] = None


class StressTestRunner:
    """压测运行器"""

    def __init__(self, url: str, concurrency: int, total_requests: int,
                 prompt: str, timeout: int, api_key: str, model: str):
        self.url = url
        self.concurrency = concurrency
        self.total_requests = total_requests
        self.prompt = prompt
        self.timeout = timeout
        self.api_key = api_key
        self.model = model
        self.metrics: List[RequestMetrics] = []
        self.console = Console()
        self.completed = 0
        self.success_count = 0

    async def _send_request(self, session: aiohttp.ClientSession) -> RequestMetrics:
        """发送单个请求"""
        metric = RequestMetrics()
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": self.prompt}],
            "stream": True,
        }

        start_time = time.time()
        first_token_time = None

        try:
            async with session.post(
                self.url,
                json=payload,
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            ) as response:
                response.raise_for_status()

                async for line in response.content:
                    if not line:
                        continue

                    line = line.decode('utf-8').strip()
                    if not line.startswith('data: '):
                        continue

                    data = line[6:]
                    if data == '[DONE]':
                        break

                    try:
                        chunk = json.loads(data)
                        if first_token_time is None:
                            first_token_time = time.time()
                            metric.ttft = first_token_time - start_time

                        if 'choices' in chunk and len(chunk['choices']) > 0:
                            delta = chunk['choices'][0].get('delta', {})
                            if 'content' in delta:
                                metric.tokens_generated += 1
                    except json.JSONDecodeError:
                        continue

                metric.total_latency = time.time() - start_time
                metric.success = True

        except asyncio.TimeoutError:
            metric.error = "Timeout"
        except aiohttp.ClientError as e:
            metric.error = str(e)
        except Exception as e:
            metric.error = str(e)

        return metric

    async def _worker(self, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore):
        """工作协程"""
        async with semaphore:
            metric = await self._send_request(session)
            self.metrics.append(metric)
            self.completed += 1
            if metric.success:
                self.success_count += 1

    def _create_dashboard(self) -> Panel:
        """创建实时仪表盘"""
        table = Table(show_header=False, box=None)

        progress_pct = (self.completed / self.total_requests) * 100
        table.add_row(f"进度: {self.completed}/{self.total_requests} ({progress_pct:.1f}%)")
        table.add_row(f"并发: {self.concurrency}")

        if self.metrics:
            latencies = [m.total_latency for m in self.metrics if m.success]
            ttfts = [m.ttft for m in self.metrics if m.success and m.ttft > 0]
            tokens = [m.tokens_generated for m in self.metrics if m.success]

            if latencies:
                p50 = calculate_percentile(latencies, 50)
                p90 = calculate_percentile(latencies, 90)
                p99 = calculate_percentile(latencies, 99)
                table.add_row("")
                table.add_row(f"P50: {format_latency(p50)} | P90: {format_latency(p90)} | P99: {format_latency(p99)}")

            if ttfts:
                avg_ttft = sum(ttfts) / len(ttfts)
                table.add_row(f"TTFT平均: {format_latency(avg_ttft)}")

            if tokens:
                avg_tokens = sum(tokens) / len(tokens)
                total_time = sum(latencies)
                if total_time > 0:
                    tokens_per_sec = sum(tokens) / total_time
                    table.add_row(f"平均Token数: {avg_tokens:.1f} | Token/s: {tokens_per_sec:.1f}")

            success_rate = calculate_success_rate(self.completed, self.success_count)
            table.add_row(f"成功率: {success_rate:.1f}%")

        return Panel(table, title="🚀 LLM压测仪表盘", border_style="cyan")

    async def run(self):
        """执行压测"""
        self.console.print(f"\n[cyan]开始压测: {self.url}[/cyan]")
        self.console.print(f"并发数: {self.concurrency} | 总请求数: {self.total_requests}\n")

        semaphore = asyncio.Semaphore(self.concurrency)

        async with aiohttp.ClientSession() as session:
            with Live(self._create_dashboard(), refresh_per_second=4, console=self.console) as live:
                tasks = [
                    asyncio.create_task(self._worker(session, semaphore))
                    for _ in range(self.total_requests)
                ]

                while self.completed < self.total_requests:
                    await asyncio.sleep(0.25)
                    live.update(self._create_dashboard())

                await asyncio.gather(*tasks)
                live.update(self._create_dashboard())

        self.console.print("\n[green]压测完成![/green]\n")
        self._print_final_report()

    def _print_final_report(self):
        """打印最终报告"""
        latencies = [m.total_latency for m in self.metrics if m.success]
        ttfts = [m.ttft for m in self.metrics if m.success and m.ttft > 0]

        if latencies:
            self.console.print(f"总请求数: {self.total_requests}")
            self.console.print(f"成功: {self.success_count} | 失败: {self.total_requests - self.success_count}")
            self.console.print(f"成功率: {calculate_success_rate(self.total_requests, self.success_count):.2f}%")
            self.console.print(f"\nP50延迟: {format_latency(calculate_percentile(latencies, 50))}")
            self.console.print(f"P90延迟: {format_latency(calculate_percentile(latencies, 90))}")
            self.console.print(f"P99延迟: {format_latency(calculate_percentile(latencies, 99))}")

            if ttfts:
                self.console.print(f"\nTTFT平均: {format_latency(sum(ttfts) / len(ttfts))}")
