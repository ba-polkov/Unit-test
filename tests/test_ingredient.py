import pytest
from pages.ingredient import Ingredient
from pages.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_ingredient_constructor_sets_values():
    type_ = INGREDIENT_TYPE_SAUCE
    name = "Hot Sauce"
    price = 100
    ingredient = Ingredient(type_, name, price)
    assert ingredient.get_type() == type_
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price


@pytest.mark.parametrize("ingredient_type,name,price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300)
])
def test_ingredient_data(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == priceice