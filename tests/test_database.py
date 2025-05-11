import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def db():
    return Database()


def test_available_buns_count(db):
    buns = db.available_buns()
    assert len(buns) == 3
    assert [bun.name for bun in buns] == ["black bun", "white bun", "red bun"]


def test_available_ingredients_count(db):
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6


@pytest.mark.parametrize("index, name, price", [
    (0, "hot sauce", 100),
    (1, "sour cream", 200),
    (2, "chili sauce", 300),
    (3, "cutlet", 100),
    (4, "dinosaur", 200),
    (5, "sausage", 300),
])
def test_ingredient_data(db, index, name, price):
    ingredient = db.available_ingredients()[index]
    assert ingredient.name == name
    assert ingredient.price == price


def test_ingredient_types(db):
    ingredients = db.available_ingredients()
    sauces = ingredients[:3]
    fillings = ingredients[3:]

    for sauce in sauces:
        assert sauce.type == INGREDIENT_TYPE_SAUCE

    for filling in fillings:
        assert filling.type == INGREDIENT_TYPE_FILLING
