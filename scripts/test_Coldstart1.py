import pytest


@pytest.fixture
def test_pass():
    ints = 1
    assert ints == 1
