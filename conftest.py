import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


# фикстура создания булки
@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = "White bun"
    mock_bun.price = 30
    return mock_bun


# фикстура создания бургера = булка + ингредиенты
@pytest.fixture
def burger_with_bun_and_two_ingredients():
    burger = Burger()
    bun = Bun("White bun", 30)
    burger.set_buns(bun)
    burger.add_ingredient(INGREDIENT_TYPE_FILLING)
    burger.add_ingredient(INGREDIENT_TYPE_SAUCE)
    return burger
    

# фикстура создания бургера: булка (название, цена) + ингредиент (название, цена)
@pytest.fixture
def create_burger_with_names_and_prices():
    burger = Burger()
    bun = Bun("White bun", 30)
    burger.set_buns(bun)
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sause", 20)
    burger.add_ingredient(ingredient)
    return burger
