# Python Project Template

This is a [cookiecutter] template for creating Python projects.

## Usage

```bash
pip install cookiecutter # if not done already
cookiecutter gh:neighthan/cookiecutter-pytemplate
```

See the `demo-project` directory for an example project created from this template. The directory structure is shown below.

```{directory_structure}
demo-project
├── demo_project
│   └── __init__.py
├── .gitignore
├── LICENSE
├── .pre-commit-config.yaml
├── pyproject.toml
├── pytest.ini
├── README.md
└── tests
    └── .gitkeep
```

### Features

#### Formatting

We use [black] for formatting through [pre-commit] (see `.pre-commit-config.yaml`) which will use a pre-commit hook in `git` to run `black` on all staged Python files. If formatting changes are needed, the files will be modified and the commit won't succeed. Just `git add` the modified files and then you can commit.

If there's a problem where you really need to commit a file without formatting, you can use `git commit -n` to skip pre-commit hooks.

After `cookiecutter` is finished, we run (as a post-gen hook)

```bash
git init
# stop here if skip_poetry_install == "y"
# see more about poetry below
poetry install
poetry run pre-commit install
```

This ensures that you won't forget to install the `pre-commit` hook and sets up the virtual environment. If you do skip the `poetry` install step, make sure to do this yourself later (this should ideally only be skipped when unneeded for testing / the demo project; it does take a minute).

[black]: https://github.com/ambv/black
[cookiecutter]: https://github.com/audreyr/cookiecutter
[pre-commit]: https://github.com/pre-commit/pre-commit
