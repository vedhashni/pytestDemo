import pytest


@pytest.fixture(scope="class")
def setup():
    print("first one")
    yield
    print("last one")