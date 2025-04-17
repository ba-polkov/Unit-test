# tests/test_ingredient.py

from praktikum.ingredient import Ingredient


def test_ingredient_get_price():
    ingredient = Ingredient("SAUCE", "BBQ", 50.0)
    assert ingredient.get_price() == 50.0, "Метод get_price должен возвращать цену ингредиента"


def test_ingredient_get_name():
    ingredient = Ingredient("FILLING", "Bacon", 70.0)
    assert ingredient.get_name() == "Bacon", "Метод get_name должен возвращать имя ингредиента"


def test_ingredient_get_type():
    ingredient = Ingredient("SAUCE", "Ketchup", 30.0)
    assert ingredient.get_type() == "SAUCE", "Метод get_type должен возвращать тип ингредиента"
