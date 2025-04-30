
from praktikum.ingredient import *
from praktikum.ingredient_types import *

def test_ingredient_initialization():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Сыр", 14.50)

    assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
    assert ingredient.get_name() == "Сыр"
    assert ingredient.get_price() == 14.50


def test_ingredient_sauce_type():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Кетчуп", 2.20)

    assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredient.get_name() == "Кетчуп"
    assert ingredient.get_price() == 2.20


def test_ingredient_filling_type():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Лук", 1.00)

    assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
    assert ingredient.get_name() == "Лук"
    assert ingredient.get_price() == 1.00


def test_ingredient_price():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Помидор", 19.75)

    assert ingredient.get_price() == 19.75


def test_ingredient_name():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Континентальный", 19.30)

    assert ingredient.get_name() == "Континентальный"