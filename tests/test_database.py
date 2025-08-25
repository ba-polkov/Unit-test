import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize('name, expected_count', 
        [
        ('black bun', 1), ('white bun', 1), ('red bun', 1),
        ('brown bun', 0), ('snowy bun', 0),
        ])
    def test_available_buns_items(self, database, name, expected_count):
        buns = database.available_buns()
        count = len(list(filter(lambda e: e.name == name, buns)))
        assert count == expected_count

    @pytest.mark.parametrize('type, name, expected_count',
        [
            (INGREDIENT_TYPE_SAUCE, 'hot sauce', 1),
            (INGREDIENT_TYPE_SAUCE, 'sour cream', 1),
            (INGREDIENT_TYPE_SAUCE, 'dummy sauce', 0),
            (INGREDIENT_TYPE_FILLING, 'cutlet', 1),
            (INGREDIENT_TYPE_FILLING, 'dinosaur', 1),
            (INGREDIENT_TYPE_FILLING, 'no name', 0),
            ('WRONG TYPE', 'cutlet', 0),
        ])
    def test_available_ingredients_items(self, database, type, name, expected_count):
        ingredients = database.available_ingredients()
        count = len(list(filter(lambda e: e.type == type and e.name == name, ingredients)))
        assert count == expected_count
