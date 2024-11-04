from ya_praktikum.ingredient import Ingredient
from ya_praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_ingredient_initialization(ingredient_data):
    ingredient_type, name, price = ingredient_data
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.type == ingredient_type
    assert ingredient.name == name
    assert ingredient.price == price

def test_get_price():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "barbecue sauce", 50)
    assert ingredient.get_price() == 50

def test_get_name():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "chicken", 100)
    assert ingredient.get_name() == "chicken"

def test_get_type():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "mustard", 30)
    assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
