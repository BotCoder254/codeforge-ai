# CodeForge AI

![CodeForge AI Logo](/media/Sentinel%20Bot.png)

CodeForge AI is an advanced code generation tool powered by state-of-the-art AI models. It helps developers quickly generate code in multiple programming languages, streamlining the development process and boosting productivity.

## Features

- 🚀 Multi-language code generation
- 🧠 Support for multiple AI models
- 🎨 Syntax highlighting and code preview
- 🌓 Dark mode support (TO BE IMPLEMENTED)
- 🐙 GitHub integration
- 📁 Local Git repository support
- 🕰️ Code history and version management (TO BE IMPLEMENTED)
- 🖥️ User-friendly, responsive interface

## Quick Start

1. Clone this repository:
2. create a virtual directory:
` python -m venv virtual `
3. If you Face Any Error Run the following command:
` Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

4. activate the virtual directory:
`virtual\Scripts\activate`

5. Install dependencies: (pip install -r requirements.txt)

6. Set up your environment variables in a `.env` file:
`TOGETHER_API_KEY=your_together_api_key_here
GITHUB_TOKEN=your_github_personal_access_token_here`

7. Run CodeForge AI:
`streamlit run codeforge.py`

## Code Structures and Variables for CodeForge

`AI_MODELS = [
    "mistralai/Mistral-7B-Instruct-v0.3",
    "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
]`

`
 extensions = {
        "Python": "py", "JavaScript": "js", "HTML": "html", "CSS": "css",
        "Java": "java", "C++": "cpp", "C#": "cs", "Ruby": "rb", "Go": "go",
        "Swift": "swift", "Kotlin": "kt", "Rust": "rs", "PHP": "php",
        "TypeScript": "ts", "Scala": "scala", "Dart": "dart", "Lua": "lua"
    }
    return extensions.get(lang, "txt")
`

`LANGUAGES = [
    "Python", "JavaScript", "HTML", "CSS", "Java", "C++", "C#", "Ruby", "Go",
    "Swift", "Kotlin", "Rust", "PHP", "TypeScript", "Scala", "Dart", "Lua"
]`








## Documentation

For detailed information on installation, usage, and configuration, please refer to our [comprehensive documentation](/docs/index.md).

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

CodeForge AI is released under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/BotCoder254/codeforge-ai/issues) on our GitHub repository.

---

Built with ❤️ by the Telvin Teum