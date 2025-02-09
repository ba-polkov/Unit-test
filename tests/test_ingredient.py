import pytest
from practikum.ingredient import Ingredient
from practikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from practikum.constants import H_NAME_SAUSE, H_PRICE_SAUSE, H_NAME_FILLING, H_PRICE_FILLING, H_INGREDIENTS


# Тестируем получение цены ингредиента
def test_get_price():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, H_NAME_SAUSE, H_PRICE_SAUSE)
    assert ingredient.get_price() == H_PRICE_SAUSE, "Метод get_price() возвращает неверную цену."

# Тестируем получение имени ингредиента
def test_get_name():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 30.0)
    assert ingredient.get_name() == "sour cream", "Метод get_name() возвращает неверное имя."

# Тестируем получение типа ингредиента
def test_get_type():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, H_NAME_FILLING, H_PRICE_FILLING)
    assert ingredient.get_type() == INGREDIENT_TYPE_FILLING, "Метод get_type() возвращает неверный тип."


# Используем параметризацию для тестирования нескольких случаев
@pytest.mark.parametrize("ingredient_type, name, price", H_INGREDIENTS)
def test_ingredient_parametrized_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price, "Метод get_price() возвращает неверную цену."
    assert ingredient.get_name() == name, "Метод get_name() возвращает неверное имя."
    assert ingredient.get_type() == ingredient_type, "Метод get_type() возвращает неверный тип."

