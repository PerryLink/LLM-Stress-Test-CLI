# LLM Stress Test CLI

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Poetry](https://img.shields.io/badge/poetry-managed-blue.svg)](https://python-poetry.org/)

A professional concurrent stress testing tool for Large Language Models. Test P99 latency, TTFT (Time To First Token), and token generation speed of your deployed models.

一个专业的大语言模型并发压测工具。测试部署模型的P99延迟、首字延迟(TTFT)和Token生成速度。

---

## English

### Features

- ⚡ High-concurrency async stress testing (based on asyncio + aiohttp)
- 📊 Real-time terminal dashboard (powered by Rich library)
- 📈 Accurate performance metrics (P50/P90/P99 latency, TTFT, Token/s)
- 🎯 Streaming API support (OpenAI-compatible format)
- 🔧 Simple and easy-to-use CLI interface

### Quick Start

#### Installation

```bash
# Clone the repository
git clone https://github.com/PerryLink/llm-stress-test-cli.git
cd llm-stress-test-cli

# Install dependencies
poetry install

# Or use pip
pip install -e .
```

#### Usage

```bash
# Test local API
poetry run llm-stress-test --url http://localhost:8000/v1/chat/completions \
  --concurrency 10 --requests 50

# Test OpenAI API
poetry run llm-stress-test --url https://api.openai.com/v1/chat/completions \
  --api-key sk-xxx --concurrency 100 --requests 1000
```

#### Parameters

- `--url`: API endpoint URL (required)
- `--concurrency`: Number of concurrent requests (default: 100)
- `--requests`: Total number of requests (default: 1000)
- `--prompt`: Test prompt (default: "Hello")
- `--timeout`: Request timeout in seconds (default: 30)
- `--api-key`: API key (optional)
- `--model`: Model name (default: "gpt-3.5-turbo")

#### Output Example

```
┌─────────────────────────────────────┐
│  🚀 LLM压测仪表盘                    │
├─────────────────────────────────────┤
│  进度: 800/1000 (80.0%)             │
│  并发: 100                          │
│                                     │
│  P50: 120.5ms | P90: 450.2ms | P99: 890.1ms│
│  TTFT平均: 85.3ms                   │
│  平均Token数: 42.5 | Token/s: 45.2  │
│  成功率: 98.5%                      │
└─────────────────────────────────────┘
```

### Project Structure

```
llm-stress-test-cli/
├── .github/
│   └── workflows/          # CI/CD workflows
├── src/
│   └── llm_stress_test_cli/
│       ├── __init__.py     # Package initialization
│       ├── __main__.py     # Entry point
│       ├── cli.py          # CLI argument parsing
│       ├── core.py         # Core stress testing engine
│       └── utils.py        # Utility functions
├── tests/                  # Unit tests
├── .gitignore
├── LICENSE                 # Apache 2.0 License
├── README.md
└── pyproject.toml          # Poetry configuration
```

### Tech Stack

- **Async Concurrency**: asyncio + aiohttp for true high concurrency
- **Real-time Visualization**: Rich library for professional terminal UI
- **Accurate Statistics**: numpy for P99 latency and other statistical metrics
- **Streaming Processing**: SSE streaming response support with precise TTFT measurement

### Development

#### Run Tests

```bash
poetry run pytest tests/ -v
```

#### Code Formatting

```bash
poetry run black src/
poetry run ruff check src/
```

### License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.

Copyright 2026 Chance Dean <novelnexusai@outlook.com>

### Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

---

## 中文

### 核心功能

- ⚡ 高并发异步压测（基于 asyncio + aiohttp）
- 📊 实时终端仪表盘（使用 Rich 库）
- 📈 精确的性能指标（P50/P90/P99延迟、TTFT、Token/s）
- 🎯 支持流式API（OpenAI兼容格式）
- 🔧 简单易用的CLI接口

### 快速开始

#### 安装

```bash
# 克隆仓库
git clone https://github.com/PerryLink/llm-stress-test-cli.git
cd llm-stress-test-cli

# 安装依赖
poetry install

# 或使用pip
pip install -e .
```

#### 使用示例

```bash
# 测试本地API
poetry run llm-stress-test --url http://localhost:8000/v1/chat/completions \
  --concurrency 10 --requests 50

# 测试OpenAI API
poetry run llm-stress-test --url https://api.openai.com/v1/chat/completions \
  --api-key sk-xxx --concurrency 100 --requests 1000
```

#### 参数说明

- `--url`: API端点URL（必需）
- `--concurrency`: 并发数（默认: 100）
- `--requests`: 总请求数（默认: 1000）
- `--prompt`: 测试提示词（默认: "Hello"）
- `--timeout`: 请求超时时间，秒（默认: 30）
- `--api-key`: API密钥（可选）
- `--model`: 模型名称（默认: "gpt-3.5-turbo"）

#### 输出示例

```
┌─────────────────────────────────────┐
│  🚀 LLM压测仪表盘                    │
├─────────────────────────────────────┤
│  进度: 800/1000 (80.0%)             │
│  并发: 100                          │
│                                     │
│  P50: 120.5ms | P90: 450.2ms | P99: 890.1ms│
│  TTFT平均: 85.3ms                   │
│  平均Token数: 42.5 | Token/s: 45.2  │
│  成功率: 98.5%                      │
└─────────────────────────────────────┘
```

### 项目结构

```
llm-stress-test-cli/
├── .github/
│   └── workflows/          # CI/CD工作流
├── src/
│   └── llm_stress_test_cli/
│       ├── __init__.py     # 包初始化
│       ├── __main__.py     # 入口点
│       ├── cli.py          # CLI参数解析
│       ├── core.py         # 核心压测引擎
│       └── utils.py        # 工具函数
├── tests/                  # 单元测试
├── .gitignore
├── LICENSE                 # Apache 2.0许可证
├── README.md
└── pyproject.toml          # Poetry配置
```

### 技术架构

- **异步并发**: asyncio + aiohttp 实现真正的高并发
- **实时可视化**: Rich 库打造专业的终端UI
- **精确统计**: numpy 计算P99延迟等统计指标
- **流式处理**: 支持SSE流式响应，精确测量TTFT

### 开发

#### 运行测试

```bash
poetry run pytest tests/ -v
```

#### 代码格式化

```bash
poetry run black src/
poetry run ruff check src/
```

### 许可证

Apache License 2.0 - 详见 [LICENSE](LICENSE) 文件。

版权所有 2026 Chance Dean <novelnexusai@outlook.com>

### 贡献

查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。
