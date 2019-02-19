from datetime import datetime
from pathlib import Path

github_username = "{{cookiecutter.github_username}}"
project_name = "{{cookiecutter.project_name}}"
Path(project_name).rename(project_name.replace("-", "_"))

license_file = Path("LICENSE")
license_text = license_file.read_text()
license_file.write_text(license_text.replace("<<year>>", str(datetime.now().year)))

setup_file = Path("setup.py")
setup_text = setup_file.read_text()

url = ""
if github_username:
    url = f"https://github.com/{github_username}/{project_name}"

setup_file.write_text(setup_text.replace("<<url>>", url))
