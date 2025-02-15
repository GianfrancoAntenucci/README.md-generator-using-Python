from InquirerPy import prompt
from rich.console import Console

# Initialize console
console = Console()

# Questions for user input
questions = [
    {"type": "input", "name": "title", "message": "Project Title:"},
    {"type": "input", "name": "description", "message": "Project Description:"},
    {"type": "input", "name": "installation", "message": "Installation Instructions:"},
    {"type": "input", "name": "usage", "message": "Usage Instructions:"},
    {"type": "rawlist", "name": "license", "message": "Choose a license:", "choices": [
        "MIT License", "Apache License 2.0", "GNU GPL v3", "LGPL v3", "MPL 2.0", "Creative Commons", "Unlicense"], "default": "MIT License"},
    {"type": "input", "name": "author", "message": "Author/Contact Information:"}
]

# Get user responses
answers = prompt(questions)

# Generate README content
readme_content = f"""# {answers['title']}

## Description
{answers['description']}

## Installation
```
{answers['installation']}
```

## Usage
```
{answers['usage']}
```

## License
This project is licensed under the {answers['license']}.

## Author
{answers['author']}
"""

# Write to README.md file
with open("README.md", "w") as file:
    file.write(readme_content)

# Success message
console.print("[bold green]README.md successfully generated![/bold green]")
