# Python Project Template

This is a [cookiecutter][cookiecutter] template for creating Python projects.

## Usage

```bash
pip install cookiecutter # if not done already
cookiecutter gh:neighthan/cookiecutter-pytemplate
```

See the `demo-project` directory for an example project created from this template. The directory structure is shown below.

```{directory_structure}
demo-project
├── .cookie_cutter.json
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

[cookiecutter]: https://github.com/audreyr/cookiecutter
