import pytest


@pytest.fixture(scope="class")   # this scope is to execute fixture before and after class (just once)
def setup():
    print("i will execute first")
    yield
    print("i will execute last")


@pytest.fixture()
def dataload():            # data driven fixture example
    print("user profile data")
    return["Pooja", "Kale", "Bavdhan"]     # return statement to load data in test case


@pytest.fixture(params=[("chrome", "pooja"), ("firefox", "mohan"), ("IE", "kale")])   # parameterized fixture with multiple data sets
def crossbrowser(request):    # request is an object of fixture
    return request.param




