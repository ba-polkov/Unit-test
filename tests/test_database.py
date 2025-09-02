import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def db():
    return Database()


def test_available_buns_returns_list_of_buns(db):
    buns = db.available_buns()
    assert isinstance(buns, list)
    assert all(isinstance(bun, Bun) for bun in buns)
    assert len(buns) > 0


def test_available_ingredients_returns_list_of_ingredients(db):
    ingredients = db.available_ingredients()
    assert isinstance(ingredients, list)
    assert all(isinstance(ing, Ingredient) for ing in ingredients)
    types = {ing.get_type() for ing in ingredients}
    assert INGREDIENT_TYPE_SAUCE in types
    assert INGREDIENT_TYPE_FILLING in types
