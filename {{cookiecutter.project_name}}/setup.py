import setuptools
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setuptools.setup(
    name="{{cookiecutter.project_name}}",
    version="0.0.1",
    author="{{cookiecutter.full_name}}",
    author_email="{{cookiecutter.email}}",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="<<url>>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: {{cookiecutter.python_version}}",
        "License :: OSI Approved :: MIT License",
    ],
)
