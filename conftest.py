import pytest

from Engine2D.engine2D import Engine2D


@pytest.fixture
def engine():
    return Engine2D()
