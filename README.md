# ðŸ›¡ï¸ Guardian AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![AI Powered](https://img.shields.io/badge/AI-Powered-brightgreen.svg)](#)

**Guardian AI** is your autonomous senior engineer and security researcher. It uses Google's Gemini Pro to provide deep, actionable code reviews for both local files and GitHub Pull Requests.

## ðŸš€ Key Features
- **Intelligent Reviews:** Analyzes bugs, security, performance, and style.
- **GitHub Integration:** Review entire Pull Requests with a single command.
- **Rich Output:** Beautiful terminal formatting using `rich`.
- **Wide Language Support:** Support for Python, JS, TS, Go, Java, C++, Rust, and more.

## ðŸ› ï¸ Installation
```bash
pip install typer google-generativeai rich PyGithub
```

## ðŸ’» Usage
Set your API keys first:
```bash
export GEMINI_API_KEY="your_gemini_key"
export GITHUB_TOKEN="your_github_token"
```

### Review a Local File
```bash
python guardian_ai.py review path/to/code.py
```

### Review a GitHub Pull Request
```bash
python guardian_ai.py pr owner/repo PR_NUMBER
```

## ðŸ¤ Contributing
Join us in making code reviews smarter! Open an issue or submit a PR to help Guardian grow.

---
Built with ðŸ§  by [David Selorm Walker](https://github.com/selormwalker)
