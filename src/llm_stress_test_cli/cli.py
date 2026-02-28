"""CLI参数解析"""

import click
import asyncio
from llm_stress_test_cli.core import StressTestRunner


@click.command()
@click.option("--url", required=True, help="API端点URL")
@click.option("--concurrency", default=100, help="并发数")
@click.option("--requests", default=1000, help="总请求数")
@click.option("--prompt", default="Hello", help="测试提示词")
@click.option("--timeout", default=30, help="请求超时时间(秒)")
@click.option("--api-key", default="", help="API密钥")
@click.option("--model", default="gpt-3.5-turbo", help="模型名称")
def main(url, concurrency, requests, prompt, timeout, api_key, model):
    """LLM压测工具 - 测试大模型的P99延迟和Token生成速度"""
    runner = StressTestRunner(
        url=url,
        concurrency=concurrency,
        total_requests=requests,
        prompt=prompt,
        timeout=timeout,
        api_key=api_key,
        model=model,
    )
    asyncio.run(runner.run())


if __name__ == "__main__":
    main()
