

![CodeForge AI Logo](/media/Sentinel%20Bot.png)

CodeForge AI is a powerful, AI-driven code generation tool that leverages state-of-the-art language models to assist developers in creating code across multiple programming languages. With an intuitive interface and seamless integration with version control systems, CodeForge AI streamlines the development process and boosts productivity.

1. Features
2. Installation
3. Usage
4. Configuration
5. API Reference
6. Contributing
7. License


# Features

1. Multi-language code generation
2. Support for multiple AI models
3. Syntax highlighting and code preview
4. Dark mode support
5. GitHub integration
6. Local Git repository support
7. Code history and version management
8. User-friendly, responsive interface

# Installation

## Prerequisites

1. Python 3.7 or higher
2. pip (Python package manager)

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

This will launch the Streamlit GUI in your default web browser. From there, you can:

1. Select the target programming language(s)
2. Choose an AI model
3. Enter your code description
4. Generate code
5. Preview and edit the generated code
6. Save or push the code to version control systems

# Configuration
CodeForge AI can be customized by modifying the Edited parts. You can adjust the following settings:

1. AI_MODELS: List of available AI models
2. LANGUAGES: Supported programming languages
3. DEFAULT_THEME: Default theme (light or dark)

# API Reference
generate_code(state)
Generates code based on the user input and selected languages.

state: The current application state

push_to_github(state)
Pushes generated code to a GitHub repository.

state: The current application state

save_code(state)
Saves the generated code locally.(TO BE IMPLEMENTED)

state: The current application state

load_code(state)
Loads previously saved code.(TO BE IMPLENTED)

state: The current application state

# Contributing
We welcome contributions to CodeForge AI! Please follow these steps to contribute:

1. Fork the repository
2.  a new branch (git checkout -b feature/your-feature-name)
3. Make your changes
4. Commit your changes (git commit -am 'Add some feature')
5.  to the branch (git push origin feature/your-feature-name)
6. Create a new Pull Request

Please ensure your code adheres to our coding standards and includes appropriate tests.
License
## CodeForge AI is released under the MIT License. See the LICENSE file for details