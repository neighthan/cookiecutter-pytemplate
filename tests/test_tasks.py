import sys
from pathlib import Path
import pytest

tasks_dir = Path(__file__).parents[1] / "{{cookiecutter.project_name}}"
sys.path.append(str(tasks_dir))

from tasks import _get_dev_num


class TestBuild:
    @pytest.mark.no_cap
    def test_get_dev_num(self):
        # this test only works if no capturing of stdout is done, but
        # capfd.disabled() and capsys.disabled() don't fix it; need
        # to run pytest -s for it to work

        project_name = "gpu-utils"
        version = "0.2.1"
        assert _get_dev_num(project_name, version) == 10
