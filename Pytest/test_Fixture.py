import pytest


@pytest.mark.usefixtures("setup")    # this is to make fixture available for all test cases or methods in file
class TestExample:

    def test_fixture1(self):
        print("i will execute test steps")

    def test_fixture2(self):
        print("i will execute test steps")

    def test_fixture3(self):
        print("i will execute test steps")

    def test_fixture4(self):
        print("i will execute test steps")
