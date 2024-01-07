from pathlib import Path

from pytest import fixture


@fixture
def resource_dir():
    return Path.cwd() / "tests" / "resources"
