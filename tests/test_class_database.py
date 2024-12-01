from database import Database
from bun import Bun
from ingredient import Ingredient

def test_database_init():
    db = Database()
    assert len(db.buns) == 3
    assert len(db.ingredients) == 6

def test_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3
    assert all(isinstance(bun, Bun) for bun in buns)

def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)