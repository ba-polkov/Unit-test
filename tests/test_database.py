import pytest
from praktikum.database import Database



def test_available_buns_and_ingredients():
    db = Database()
    buns = db.available_buns()
    ingredients = db.available_ingredients()

    assert isinstance(buns, list)
    assert all(isinstance(b, type(buns[0])) for b in buns)
    assert len(buns) >= 3

    assert isinstance(ingredients, list)
    assert all(isinstance(i, type(ingredients[0])) for i in ingredients)

    names = [i.get_name() for i in ingredients]
    assert "hot sauce" in names
    assert "cutlet" in names

