#!/usr/bin/env python

import re
from pathlib import Path
from subprocess import run
from shutil import rmtree
import click
from cookiecutter.main import cookiecutter


@click.command()
@click.option("-i", "--include_invoke", default=False, is_flag=True)
def create_demo(include_invoke):
    demo_name = "demo-project"
    cookiecutter_args = {
        "project_name": demo_name,
        "description": "A demo project",
        "full_name": "Nathan Hunt",
        "email": "neighthan.hunt@gmail.com",
        "github_username": "neighthan",
        "python_version": "3.7",
        "include_invoke_tasks": "y" if include_invoke else "n",
    }

    # using overwrite_if_exists led to hook failures, so just
    # ensure there isn't an existing demo project
    demo_path = Path(__file__).parent / demo_name
    try:
        rmtree(str(demo_path))
    except FileNotFoundError:
        pass

    template_path = Path(__file__).parent

    cookiecutter(str(template_path), extra_context=cookiecutter_args, no_input=True)

    # now update the README with the (potentially new) structure
    readme = Path(__file__).parent / "README.md"
    readme_text = readme.read_text()
    old_tree_output = re.search(
        r"```\{directory_structure\}.*?```", readme_text, re.DOTALL
    )

    try:
        result = run(["tree", "-a", str(demo_path)], capture_output=True)
        new_tree_output = result.stdout.decode()
    except FileNotFoundError:  # no tree command
        return

    new_tree_output = "\n".join(new_tree_output.splitlines()[:-2])
    new_tree_output = "```{directory_structure}\n" + new_tree_output + "\n```"
    readme_text = (
        readme_text[: old_tree_output.start()]
        + new_tree_output
        + readme_text[old_tree_output.end() :]
    )
    readme.write_text(readme_text)


if __name__ == "__main__":
    create_demo()
