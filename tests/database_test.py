import pytest
from practicum.database import Database

class TestDatabase:
    def test_initialization(self):
        db = Database()
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(bun.name in ['black bun', 'white bun', 'red bun'] for bun in buns)

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(ingredient.name in ['hot sauce', 'sour cream', 'chili sauce', 
                                     'cutlet', 'dinosaur', 'sausage'] for ingredient in ingredients)