import pytest
from practicum_burgers.burger import Burger


@pytest.fixture
def burger():
    burger = Burger()
    return burger
