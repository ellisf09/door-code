# Door-Code

<!-- <p align="left">
  <img src="https://shields.io" alt="License" />
  <img src="https://shields.io" alt="Last Commit" />
  <img src="https://shields.io" alt="Python" />
  <img src="https://shields.io" alt="OpenRouter API" />
</p> -->
![GitHub License](https://img.shields.io/github/license/ellisf09/door-code)
![GitHub last commit](https://img.shields.io/github/last-commit/ellisf09/door-code)
<img src="https://skillicons.dev/icons?i=py">


A lightweight, CLI-based AI coding agent inspired by Claude Code, built in Python with OpenRouter API integration and autonomous file-system tool calling.

> **Note:** This is an experimental project. Always review file modifications before running the agent on important files.

## ✨ Features
- **Autonomous Tool Calling:** Capable of inspecting directories, reading file contents, writing code, and executing Python scripts.
- **OpenRouter Integration:** Connects to flexible LLM backends via OpenRouter.
- **Sandboxed Test Environment:** Includes a sample `calculator/` project to safely test the agent's debugging and code-generation abilities.

## 🚀 Getting Started
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd door-code
   ```
2. **Set up your environment:**
   Ensure you have Python installed and configure your OpenRouter API key in your environment variables:
   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"
   ```
3. **Run the agent:**
   ```bash
   python main.py
   ```

## 🧪 Running Tests
The repository includes unit tests for all core agent functions (`get_files_info`, `get_file_content`, `write_file`, and `run_python_file`):
```bash
python tests.py
```
