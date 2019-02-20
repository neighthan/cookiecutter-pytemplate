from pathlib import Path

project_name = "{{cookiecutter.project_name}}"
Path(project_name).rename(project_name.replace("-", "_"))
