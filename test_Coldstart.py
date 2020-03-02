import pytest


@pytest.fixture
def test_pass():
    assert 1 == 1
