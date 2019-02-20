import json
from pathlib import Path
from subprocess import run

project_name = "{{cookiecutter.project_name}}"
Path(project_name).rename(project_name.replace("-", "_"))

include_invoke_tasks = "{{cookiecutter.include_invoke_tasks}}"
if include_invoke_tasks == "n":
    Path("./tasks.py").unlink()

run(["git", "init"])
