# Python Project Template

This is a [cookiecutter] template for creating Python projects.

## Usage

```bash
# skip the first two lines if you already have cookiecutter / poetry
pip install cookiecutter
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
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

## Features

Here we give an overview of the tools used in this template. See their respective repos / web pages for full documentation.

### Package Management

We use [poetry] for package management and building.

**Package Management**

Packages are added to your project using `poetry add`; use the `-D` flag for dev dependencies. All dependencies (packages + allowed versions) will be stored in your `pyproject.toml` file. `poetry` also creates a virtual environment for your project to keep your packages isolated from those used in your other Python projects. Use `poetry shell` to start a shell in this environment when needed or `poetry run` to run a given command there. `poetry install --develop` is similar to `pip install -e .`.

**Building**

The `pyproject.toml` file (see [PEP 517] and [PEP 518]) should replace the old `setup.py` file + friends (e.g. `MANIFEST.in`). This allows other tools besides `distutils` and `setuptools` to be used for building. You can run `poetry build` to create your distribution and `poetry publish` to upload this to PyPI (or other repos that you configure), but see the [`invoke` section](###`invoke`-Tasks) below for our preferred method of building / publishing (which uses `poetry` internally).

### Formatting

We use [black] for formatting through [pre-commit] (see `.pre-commit-config.yaml`) which will use a pre-commit hook in `git` to run `black` on all staged Python files whenever you `git commit`. If formatting changes are needed, the files will be modified and the commit won't succeed. Just `git add` the modified files and then you can commit.

If there's a problem where you really need to commit a file without formatting, you can use `git commit -n` to skip pre-commit hooks.

After `cookiecutter` is finished, we run (as a post-gen hook)

```bash
git init
# stop here if skip_poetry_install == "y"
poetry install
poetry run pre-commit install
```

This ensures that you won't forget to install the `pre-commit` hook and sets up the virtual environment. If you do skip the `poetry` install step, make sure to do this yourself later (this should ideally only be skipped when unneeded for testing / the demo project; it does take a minute).

### `invoke` Tasks

We use [invoke] to run various tasks like uploading the project to PyPI / test PyPI. This is similar to the usage of phony targets in Makefiles in other projects, but we prefer to keep things in Python when possible.

* `upload`
* `update_tasks`

[black]: https://github.com/ambv/black
[cookiecutter]: https://github.com/audreyr/cookiecutter
[invoke]: https://github.com/pyinvoke/invoke/
[poetry]: https://github.com/sdispater/poetry
[pre-commit]: https://github.com/pre-commit/pre-commit
[PEP 517]: https://www.python.org/dev/peps/pep-0517/
[PEP 518]: https://www.python.org/dev/peps/pep-0518/
