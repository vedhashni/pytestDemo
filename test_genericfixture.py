import pytest


@pytest.mark.usefixtures("setup")
class TestGeneric:

    def test_Program1(self):
        print("Demo1")


    def test_Program2(self):
        print("Demo2")


    def test_Program3(self):
        print("Demo3")


    def test_Program4(self):
        print("Demo4")