#!/usr/bin/env python

from pathlib import Path
from shutil import rmtree
from cookiecutter.main import cookiecutter


def create_demo():
    demo_name = "demo-project"
    cookiecutter_args = {
        "project_name": demo_name,
        "description": "A demo project",
        "full_name": "Nathan Hunt",
        "email": "neighthan.hunt@gmail.com",
        "github_username": "neighthan",
        "python_version": "3.7",
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


if __name__ == "__main__":
    create_demo()
