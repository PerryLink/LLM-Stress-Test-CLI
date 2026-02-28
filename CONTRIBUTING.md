# Contributing to LLM Stress Test CLI

## English

### Project Status

This is currently a personal project maintained by [Chance Dean](https://github.com/PerryLink). While contributions are welcome, please note that this project is primarily developed and maintained by a single person.

### Reporting Issues

If you encounter any bugs or have feature requests:

1. Check if the issue already exists in the [Issues](https://github.com/PerryLink/llm-stress-test-cli/issues) section
2. If not, create a new issue with:
   - A clear and descriptive title
   - Detailed description of the problem or feature request
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)

### Development Environment Setup

1. Fork and clone the repository:
```bash
git clone https://github.com/PerryLink/llm-stress-test-cli.git
cd llm-stress-test-cli
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Run tests to verify setup:
```bash
poetry run pytest tests/ -v
```

### Code Standards

This project follows Python best practices:

- **PEP 8**: Follow Python's official style guide
- **Type Hints**: Use type hints where appropriate
- **Docstrings**: Add docstrings for public functions and classes
- **Testing**: Write tests for new features

#### Code Formatting

Before submitting code, format it using:

```bash
# Format code
poetry run black src/

# Check code style
poetry run ruff check src/
```

### Pull Request Process

1. Create a new branch for your feature or bugfix:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit:
```bash
git add .
git commit -m "Add: your feature description"
```

3. Push to your fork:
```bash
git push origin feature/your-feature-name
```

4. Create a Pull Request with:
   - Clear description of changes
   - Reference to related issues (if any)
   - Test results showing your changes work

5. Wait for review and address any feedback

### Commit Message Guidelines

Use clear and descriptive commit messages:

- `Add: new feature description`
- `Fix: bug description`
- `Update: improvement description`
- `Refactor: code refactoring description`
- `Docs: documentation changes`
- `Test: test-related changes`

---

## 中文

### 项目状态

这是一个由 [Chance Dean](https://github.com/PerryLink) 个人维护的项目。虽然欢迎贡献，但请注意这个项目主要由一个人开发和维护。

### 报告问题

如果你遇到任何bug或有功能请求：

1. 检查 [Issues](https://github.com/PerryLink/llm-stress-test-cli/issues) 中是否已存在该问题
2. 如果没有，创建新issue并包含：
   - 清晰描述性的标题
   - 问题或功能请求的详细描述
   - 重现步骤（针对bug）
   - 期望行为 vs 实际行为
   - 你的环境信息（操作系统、Python版本等）

### 开发环境搭建

1. Fork并克隆仓库：
```bash
git clone https://github.com/PerryLink/llm-stress-test-cli.git
cd llm-stress-test-cli
```

2. 安装Poetry（如果尚未安装）：
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. 安装依赖：
```bash
poetry install
```

4. 运行测试验证设置：
```bash
poetry run pytest tests/ -v
```

### 代码规范

本项目遵循Python最佳实践：

- **PEP 8**: 遵循Python官方风格指南
- **类型提示**: 在适当的地方使用类型提示
- **文档字符串**: 为公共函数和类添加文档字符串
- **测试**: 为新功能编写测试

#### 代码格式化

提交代码前，使用以下命令格式化：

```bash
# 格式化代码
poetry run black src/

# 检查代码风格
poetry run ruff check src/
```

### Pull Request流程

1. 为你的功能或bug修复创建新分支：
```bash
git checkout -b feature/your-feature-name
```

2. 进行更改并提交：
```bash
git add .
git commit -m "Add: 你的功能描述"
```

3. 推送到你的fork：
```bash
git push origin feature/your-feature-name
```

4. 创建Pull Request并包含：
   - 清晰的更改描述
   - 相关issue的引用（如果有）
   - 显示你的更改有效的测试结果

5. 等待审查并处理任何反馈

### 提交信息指南

使用清晰描述性的提交信息：

- `Add: 新功能描述`
- `Fix: bug描述`
- `Update: 改进描述`
- `Refactor: 代码重构描述`
- `Docs: 文档更改`
- `Test: 测试相关更改`

---

## Contact / 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com

Thank you for contributing! / 感谢你的贡献！
