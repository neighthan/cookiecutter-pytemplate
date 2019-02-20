import re
import invoke
from pathlib import Path
from time import sleep
from invoke.exceptions import UnexpectedExit

_version_pattern = re.compile(
    r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<micro>\d+)(\.(?P<suffix>[A-z0-9]+))?"
)


@invoke.task
def upload(ctx, test: bool = False, n_download_tries: int = 3):
    """
    Assumptions:
    * the project is structured as <name>/<name'> where <name>
      is the project name and <name'> is the same as <name> except with any "-"
      replaced by "_". `tasks.py` should be stored in <name>.
    * the version is stored in <name>/<name'>/_version.py and that
      this file only contains `__version__ = "<version>"` where <version> is of the
      format major.minor.micro (with optional suffix such as dev0).
    * If you use the test flag, you have at least the following in `~/.pypirc`:
      [testpypi]
      repository: https://test.pypi.org/legacy/
    """

    # TODO - don't upload if test is False and there are unstaged changes to
    # tracked files unless --force is given

    # TODO - add a git tag to the most recent commit that says what the version is
    # https://stackoverflow.com/questions/4404172/how-to-tag-an-older-commit-in-git

    project_name = "{{cookiecutter.project_name}}"
    project_root = str(Path(__file__).parent.resolve())
    sleep_time = 5

    if test:
        # add dev if lacking; increment dev number if present
        # this is because test.pypi still won't let you upload the same version
        # multiple times. Doing this automates changing the version for repeat testing

        version = {}
        version_path = (
            Path(__file__).parent / project_name.replace("-", "_") / "_version.py"
        )
        exec(version_path.read_text(), version)
        original_version = version["__version__"]

        dev_num = _get_dev_num(project_name, original_version)
        version = re.fullmatch(_version_pattern, original_version)
        version = ".".join(version.groups()[:3]) + f"dev{dev_num}"

        # write back the modified version
        version_path.write_text(f'__version__ = "{version}"\n')

    try:
        cmd = f"""
        cd {project_root}

        rm -rf build
        rm -rf dist

        pip install -U setuptools wheel twine
        python setup.py sdist bdist_wheel
        twine upload {'--repository testpypi' if test else ''} dist/*

        rm -rf build
        rm -rf dist
        """

        ctx.run(cmd)
    finally:
        if test:
            version_path.write_text(f'__version__ = "{original_version}"\n')

    if not test:
        return

    for i in range(n_download_tries):
        sleep(sleep_time)
        try:
            result = ctx.run(
                f"""
                cd
                pip install --index-url https://test.pypi.org/simple/ {project_name}=={version}
                """
            )
            break
        except UnexpectedExit:
            continue


def _get_dev_num(project_name: str, current_version: str) -> int:
    # 1. read the whole suffix
    # 2. replace it by dev<dev_num>
    # 3. build and publish
    # 4. write back the original suffix
    # to determine dev_num we run pip and find the latest version that has the same
    # major.minor.micro and dev; then we increment by one.

    cmd = f"pip install --index-url https://test.pypi.org/simple {project_name}==?"
    result = invoke.run(cmd, warn=True, hide=True)

    current_version = re.fullmatch(_version_pattern, current_version)
    current_version_groups = current_version.groupdict()

    dev_num = 0
    # reverse so that we hit the latest version first
    for published_version in list(re.finditer(_version_pattern, result.stderr))[::-1]:
        groups = published_version.groupdict()
        if (
            groups["major"] == current_version_groups["major"]
            and groups["minor"] == current_version_groups["minor"]
            and groups["micro"] == current_version_groups["micro"]
            and groups["suffix"].startswith("dev")
        ):
            dev_num = int(groups["suffix"].replace("dev", "")) + 1
            break
    return dev_num
