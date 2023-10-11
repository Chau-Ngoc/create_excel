from pytest import fixture

from constants import BASE_DIR


@fixture
def resource_dir():
    return BASE_DIR / "tests" / "resources"
