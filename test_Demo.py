import pytest


@pytest.mark.smoke
def test_program1(setup):
    print("Hello")


@pytest.mark.xfail
def test_ProgramCredit():
    print("Hi")
