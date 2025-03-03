import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture  # Мок для класса Bun, который возвращает имя и цену булочки
def bun_mock():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Булочка"
    bun.get_price.return_value = 50.0
    return bun

@pytest.fixture  # Мок для класса Ingredient, который возвращает имя, цену и тип ингредиента
def ingredient_mock():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "помидор"
    ingredient.get_price.return_value = 10.0
    ingredient.get_type.return_value = "начинка"
    return ingredient
