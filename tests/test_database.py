from praktikum.database import Database

import pytest

class TestDatabase:

    @pytest.mark.parametrize('index, bun_name, bun_price', [
        (0, 'black bun', 100),
        (1, 'white bun', 200),
        (2, 'red bun', 300)
    ])
    def test_available_buns(self, index, bun_name, bun_price):
        db = Database()
        buns = db.available_buns()
        bun = buns[index]
        assert bun.get_name() == bun_name
        assert bun.get_price() == bun_price

    @pytest.mark.parametrize('index, ingredient_type, ingredient_name, ingredient_price', [
        (0, 'SAUCE', 'hot sauce', 100),
        (1, 'SAUCE', 'sour cream', 200),
        (2, 'SAUCE', 'chili sauce', 300),
        (3, 'FILLING', 'cutlet', 100),
        (4, 'FILLING', 'dinosaur', 200),
        (5, 'FILLING', 'sausage', 300)
    ])
    def test_available_ingredients(self, index, ingredient_type, ingredient_name, ingredient_price):
        db = Database()
        ingredients = db.available_ingredients()
        ingredient = ingredients[index]
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == ingredient_name
        assert ingredient.get_price() == ingredient_price

    def test_get_quantity_available_sauces(self):
        db = Database()
        ingredients = db.available_ingredients()
        sauces = [i for i in ingredients if i.get_type() == 'SAUCE']
        assert len(sauces) == 3

    def test_get_quantity_available_fillings(self):
        db = Database()
        ingredients = db.available_ingredients()
        fillings = [i for i in ingredients if i.get_type() == 'FILLING']
        assert len(fillings) == 3

    def test_get_ingredients_prices(self):
        db = Database()
        ingredients = db.available_ingredients()
        price = {i.get_name(): i.get_price() for i in ingredients}
        assert price['hot sauce'] == 100
        assert price['sour cream'] == 200
        assert price['chili sauce'] == 300
        assert price['cutlet'] == 100
        assert price['dinosaur'] == 200
        assert price['sausage'] == 300
