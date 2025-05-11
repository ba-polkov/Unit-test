import pytest
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


@pytest.fixture
#Создаем ингредиент
def ingredient():
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, 'Соус', 60)
    return ingredient
