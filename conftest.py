import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "mocked bun"
    bun.get_price.return_value = 123
    return bun

@pytest.fixture(params=[("mocked bun", 123), ("special bun", 200)])
def parametrized_mock_bun(request):
    name, price = request.param
    bun = Mock()
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun

@pytest.fixture
def mock_ingredient():
    def _create(name, type, price):
        ingredient = Mock()
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        ingredient.get_type.return_value = type
        return ingredient
    return _create

@pytest.fixture
def sample_bun():
    return Bun("sample bun", 150)

@pytest.fixture(params=[
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 80),
    (INGREDIENT_TYPE_FILLING, "cheese", 120)
])
def sample_ingredient(request):
    return Ingredient(*request.param)

@pytest.fixture
def sample_ingredients():
    return [
        Ingredient(INGREDIENT_TYPE_SAUCE, "garlic sauce", 50),
        Ingredient(INGREDIENT_TYPE_FILLING, "beef", 200),
    ]


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def prepared_burger(burger, sample_bun, sample_ingredients):
    burger.set_buns(sample_bun)
    for ingredient in sample_ingredients:
        burger.add_ingredient(ingredient)
    return burger