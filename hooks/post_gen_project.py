import json
from pathlib import Path

project_name = "{{cookiecutter.project_name}}"
Path(project_name).rename(project_name.replace("-", "_"))

include_invoke_tasks = "{{cookiecutter.include_invoke_tasks}}"
if include_invoke_tasks == "n":
    Path("./tasks.py").unlink()

# TODO - is there any better way to save all of this without needing to
# update the dict here each time cookiecutter.json is updated?
cookiecutter_dict = {
  "project_name": "{{cookiecutter.project_name}}",
  "description": "{{cookiecutter.description}}",
  "full_name": "{{cookiecutter.full_name}}",
  "email": "{{cookiecutter.email}}",
  "github_username": "{{cookiecutter.github_username}}",
  "python_version": "{{cookiecutter.python_version}}",
  "include_invoke_tasks": "{{cookiecutter.include_invoke_tasks}}"
}

Path("./.cookie_cutter.json").write_text(json.dumps(cookiecutter_dict))
