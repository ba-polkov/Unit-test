# conftest.py

import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient


@pytest.fixture
def default_bun():
    return Bun("Краторная булка N-200i", 1255)


@pytest.fixture(params=[
    ("Флюоресцентная булка R2-D3", 988),
    ("Краторная булка N-200i", 1255)
])
def parametrized_bun(request):
    return Bun(*request.param)


@pytest.fixture
def empty_burger():
    return Burger()

@pytest.fixture
def prepared_burger():
    bun = Bun("Краторная булка N-200i", 1255)
    ingredient1 = Ingredient("SAUCE", "Соус фирменный Space Sauce", 80)
    ingredient2 = Ingredient("FILLING", "Биокотлета из марсианской Магнолии", 424)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    return burger