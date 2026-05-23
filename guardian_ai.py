import typer
import google.generativeai as genai
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from github import Github

app = typer.Typer(help="Guardian AI: Your automated code reviewer.")
console = Console()

# Supported file extensions for review
SUPPORTED_EXTENSIONS = {'.py', '.js', '.ts', '.jsx', '.tsx', '.go', '.java', '.cpp', '.rs'}

def get_model():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/bold red] GEMINI_API_KEY environment variable not found.")
        raise typer.Exit(code=1)
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')

@app.command()
def review(file_path: str):
    """Review a specific file and provide AI feedback."""
    if not os.path.exists(file_path):
        console.print(f"[bold red]Error:[/bold red] File {file_path} not found.")
        return

    model = get_model()
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    prompt = f"""
    You are an expert senior software engineer and security researcher. 
    Review the following code and provide a detailed analysis focusing on:
    1. Potential bugs and logical errors.
    2. Security vulnerabilities.
    3. Performance optimizations.
    4. Code style and maintainability.

    Code to review ({file_path}):
    ```
    {content}
    ```
    
    Provide your feedback in clear, actionable Markdown.
    """

    with console.status("[bold green]Analyzing code..."):
        response = model.generate_content(prompt)
        console.print(Panel(Markdown(response.text), title=f"Guardian Review: {file_path}", border_style="blue"))

@app.command()
def pr(repo_name: str, pr_number: int):
    """Review a GitHub Pull Request."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        console.print("[bold red]Error:[/bold red] GITHUB_TOKEN environment variable not found.")
        return

    g = Github(token)
    repo = g.get_repo(repo_name)
    pr_obj = repo.get_pull(pr_number)
    model = get_model()

    console.print(f"[bold blue]Guardian is inspecting PR #{pr_number}:[/bold blue] {pr_obj.title}")

    for file in pr_obj.get_files():
        if any(file.filename.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
            if not file.patch: continue
            
            prompt = f"Review this PR diff for {file.filename}:\n\n```diff\n{file.patch}\n```"
            response = model.generate_content(prompt)
            console.print(Panel(Markdown(response.text), title=f"PR Review: {file.filename}", border_style="cyan"))

if __name__ == "__main__":
    app()
