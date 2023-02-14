import pytest


@pytest.fixture(scope='session')
def before_suite():
    print("Método executado no inicio da suíte")


@pytest.fixture(scope='session')
def after_suite(request):
    request.addfinalizer(after_suite_step)


def after_suite_step():
    print("Método executado no final da suíte")
