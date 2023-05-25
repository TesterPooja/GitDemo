import pytest


@pytest.mark.xfail   # you know this test case if failing, but you don,t want to show in report, use xfail mark
def test_addition():
    a = 2
    b = 3
    c = a + b
    assert c == 6, "Addition is incorrect"


def test_crossbrowser(crossbrowser):      # parameterized test with multiple data sets using fixtures
    print(crossbrowser)
    print(crossbrowser[1])


