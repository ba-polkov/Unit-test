import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
    
    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6
        
        # Проверяем соусы
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
        assert sauces[0].get_name() == "hot sauce"
        
        # Проверяем начинки
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
        assert fillings[0].get_name() == "cutlet"