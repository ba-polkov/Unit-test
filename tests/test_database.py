from praktikum.database import Database
from data import Data

def test_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == len(Data.BUNS)
    for i, (bun_name, bun_price) in enumerate(Data.BUNS):
        assert buns[i].get_name() == bun_name
        assert buns[i].get_price() == bun_price

def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == len(Data.INGREDIENTS)
    for i, (ingredient_type, ingredient_name, ingredient_price) in enumerate(Data.INGREDIENTS):
        assert ingredients[i].get_type() == ingredient_type
        assert ingredients[i].get_name() == ingredient_name
        assert ingredients[i].get_price() == ingredient_price
