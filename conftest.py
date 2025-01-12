import pytest
from helpers import RandomCred

@pytest.fixture(scope = "function")
def name():
    name = RandomCred.generate_random_name()
    return  name

@pytest.fixture(scope = "function")
def price():
    price = RandomCred.generate_random_float()
    return price

@pytest.fixture(scope = "function")
def type_ingredient():
    type_ingredient = RandomCred.random_choice_ingredients()
    return type_ingredient
