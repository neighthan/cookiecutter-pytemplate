import toml
from pathlib import Path

__version__ = toml.load(str(Path(__file__).parents[1] / "pyproject.toml"))["tool"][
    "poetry"
]["version"]
