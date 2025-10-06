import pytest
from data.data import expected_buns, expected_ingredients
from praktikum.database import Database

class TestDatabase:


    def test_buns_are_returned_as_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list), "Булки должны возвращаться в виде списка"

    @pytest.mark.parametrize("index, name, price", expected_buns)
    def test_buns_have_expected_names(self,index, name, price):
        db = Database()
        buns = db.available_buns()
        assert buns[index].name == name, f"Ожидалось имя булки {name}, получено {buns[index].name}"

    @pytest.mark.parametrize("index, name, price", expected_buns)
    def test_buns_have_expected_prices(self,index, name, price):
        db = Database()
        buns = db.available_buns()
        assert buns[index].price == price, f"Ожидалась цена булки {price}, получена {buns[index].price}"

    def test_ingredients_are_returned_as_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list), "Ингредиенты должны возвращаться в виде списка"

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_ingredients_have_expected_types(self, index, ingredient_type, ingredient_name, ingredient_price):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[index].type == ingredient_type, f"Ожидался тип {ingredient_type}, получен {ingredients[index].type}"

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_ingredients_have_expected_names(self, index, ingredient_type, ingredient_name, ingredient_price):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[index].name == ingredient_name, f"Ожидалось имя {ingredient_name}, получено {ingredients[index].ingredient_name}"

    @pytest.mark.parametrize("index, ingredient_type, ingredient_name, ingredient_price", expected_ingredients)
    def test_ingredients_have_expected_prices(self, index, ingredient_type, ingredient_name, ingredient_price):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[index].price == ingredient_price, f"Ожидалась цена {ingredient_price}, получена {ingredients[index].price}"