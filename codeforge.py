import streamlit as st
import os
from together import Together
import base64
from github import Github
import pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Set up Together API
client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

# Set up GitHub API
github_token = os.getenv("GITHUB_TOKEN")
g = Github(github_token) if github_token else None

# List of supported programming languages
#You can also add more languages  to make it more productive
LANGUAGES = [
    "Python", "JavaScript", "HTML", "CSS", "Java", "C++", "C#", "Ruby", "Go",
    "Swift", "Kotlin", "Rust", "PHP", "TypeScript", "Scala", "Dart", "Lua"
]

# List of supported AI models 
# Disclaimer: You can add more AI models to make it more productive following the provided documantation
AI_MODELS = [
    "mistralai/Mistral-7B-Instruct-v0.3",
    "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
]

# ASCII Art Logo
LOGO = """
   ____          _      ______                      _    ___ 
  / ___|___   __| | ___|  ____|__  _ __ __ _  ___  / \  |_ _|
 | |   / _ \ / _` |/ _ \ |__ / _ \| '__/ _` |/ _ \/_ _\  | | 
 | |__| (_) | (_| |  __/  __/ (_) | | | (_| |  __/  _  | | | 
  \____\___/ \__,_|\___|_|   \___/|_|  \__, |\___\_/ \_\|___|
                                       |___/                 
"""

def generate_code(model, languages, prompt):
    generated_code = {}
    for lang in languages:
        full_prompt = f"Generate {lang} code for: {prompt}"
        
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": full_prompt}]
            )
            generated_code[lang] = response.choices[0].message.content.strip()
        except Exception as e:
            st.error(f"Error generating code for {lang}: {e}")
            generated_code[lang] = "Error generating code"

    return generated_code

def highlight_code(code, language):
    lexer = get_lexer_by_name(language.lower(), stripall=True)
    formatter = HtmlFormatter(style="github-dark" if st.session_state.theme == "dark" else "github-light")
    return pygments.highlight(code, lexer, formatter)

def push_to_github(username, repo_name, branch, generated_code):
    try:
        if not g:
            raise Exception("GitHub token not set")
        
        user = g.get_user()
        repo = user.get_repo(repo_name)
        
        for lang, code in generated_code.items():
            file_path = f"generated_{lang.lower()}.{get_file_extension(lang)}"
            content = base64.b64encode(code.encode("utf-8")).decode("utf-8")
            
            try:
                file = repo.get_contents(file_path, ref=branch)
                repo.update_file(file_path, f"Update {lang} code", code, file.sha, branch=branch)
            except:
                repo.create_file(file_path, f"Add {lang} code", code, branch=branch)
        
        return True, "Code pushed to GitHub successfully!"
    except Exception as e:
        return False, f"GitHub push failed: {str(e)}"

def get_file_extension(lang): # you can edit and add more language and frameworks
    extensions = {
        "Python": "py", "JavaScript": "js", "HTML": "html", "CSS": "css",
        "Java": "java", "C++": "cpp", "C#": "cs", "Ruby": "rb", "Go": "go",
        "Swift": "swift", "Kotlin": "kt", "Rust": "rs", "PHP": "php",
        "TypeScript": "ts", "Scala": "scala", "Dart": "dart", "Lua": "lua"
    }
    return extensions.get(lang, "txt")

def main():
    st.set_page_config(page_title=(LOGO), page_icon="🚀", layout="medium")

    # Initialize session state
    if 'theme' not in st.session_state:
        st.session_state.theme = "light"
    if 'generated_code' not in st.session_state:
        st.session_state.generated_code = {}
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Sidebar
    st.sidebar.title("CodeForge AI")
    st.sidebar.text(LOGO)
    
    # Theme selector
    theme = st.sidebar.selectbox("Theme", ["light", "dark"], index=0 if st.session_state.theme == "light" else 1)
    if theme != st.session_state.theme:
        st.session_state.theme = theme
        try:
            st.experimental_rerun()
        except Exception as e:
            st.error(f"Error reloading the app: {e}")

    # Main content
    st.title("CodeForge AI")

    # Input section
    st.header("Input")
    selected_model = st.selectbox("Select AI Model", AI_MODELS)
    selected_languages = st.multiselect("Select Languages", LANGUAGES)
    user_input = st.text_area("Enter your code description")

    if st.button("Generate Code"):
        with st.spinner("Generating code..."):
            st.session_state.generated_code = generate_code(selected_model, selected_languages, user_input)
        
        # Add to history
        st.session_state.history.append({
            "input": user_input,
            "code": st.session_state.generated_code,
            "model": selected_model,
            "languages": selected_languages
        })

    # Generated code section
    if st.session_state.generated_code:
        st.header("Generated Code")
        for lang, code in st.session_state.generated_code.items():
            with st.expander(f"{lang} Code"):
                st.code(code, language=lang.lower())

    # Preview section
    if "HTML" in st.session_state.generated_code:
        st.header("Preview")
        st.components.v1.html(st.session_state.generated_code["HTML"], height=300)

    # GitHub integration
    st.header("GitHub Integration")
    github_username = st.text_input("GitHub Username")
    github_repo = st.text_input("GitHub Repository")
    github_branch = st.text_input("GitHub Branch", value="main")

    if st.button("Push to GitHub"):
        success, message = push_to_github(github_username, github_repo, github_branch, st.session_state.generated_code)
        if success:
            st.success(message)
        else:
            st.error(message)
            
            #TO BE IMPLEMENTED VERY SOON OR ANY SOLUTION CONTRIBUTORS FEEL FREE TO IMPLEMENT

    # # History section
    # st.header("History")
    # if st.session_state.history:
    #     selected_history = st.selectbox(
    #         "Select from history",
    #         range(len(st.session_state.history)),
    #         format_func=lambda i: f"Item {i+1}: {st.session_state.history[i]['input'][:50]}..."
    #     )
    #     if st.button("Load from History"):
    #         history_item = st.session_state.history[selected_history]
    #         st.session_state.generated_code = history_item["code"]
    #         try:
    #             st.experimental_rerun()
    #         except Exception as e:
    #             st.error(f"Error reloading the app: {e}")

if __name__ == "__main__":
    main()
