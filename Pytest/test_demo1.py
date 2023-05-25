# any pytest file should start with test_ or end with _test
# pytest method name should start with test_
# any code should be wrapped in method only
# one method is one test case and method name should be unique otherwise only latest method will be executed
# method name should be meaningful like e.g. credit card, so all credit card related tests will fall under this
# -k means regular expression (contains) used to execute specific method or test cases
# -v more info like metadata, -s logs in output
# you can run specific file with pytest <filename.py>
# fixtures are used for setup and tear down methods for test cases
# conftest file will generalize fixture for all pytest files
# datadriven and parameterization can be done with return statement in tuple format


import pytest


@pytest.mark.smoke      # mark test if you want to run specific tests or for regression, grouping tests
def test_firstProgram(setup):     # setup is fixture method from conftest file
    print("Hello")


@pytest.mark.skip      # mark skip if you want to skip any test case
def test_Greet():
    msg = "Greet"
    assert msg == "Greet", "condition do not match"


