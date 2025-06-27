import pytest
from data import expected_buns, expected_ingredients
from praktikum.database import Database

class TestDatabase:


    def test_buns_are_returned_as_list(self, db):
        buns = db.available_buns()
        assert isinstance(buns, list), "Булки должны возвращаться в виде списка"

    @pytest.mark.parametrize("index, name, price", expected_buns)
    def test_buns_have_expected_names(self, db, index, name, price):
        buns = db.available_buns()
        assert buns[index].name == name, f"Ожидалось имя булки {name}, получено {buns[index].name}"

    @pytest.mark.parametrize("index, name, price", expected_buns)
    def test_buns_have_expected_prices(self, db, index, name, price):
        buns = db.available_buns()
        assert buns[index].price == price, f"Ожидалась цена булки {price}, получена {buns[index].price}"

    def test_ingredients_are_returned_as_list(self, db):
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list), "Ингредиенты должны возвращаться в виде списка"

    @pytest.mark.parametrize("index, type_, name, price", expected_ingredients)
    def test_ingredients_have_expected_types(self, db, index, type_, name, price):
        ingredients = db.available_ingredients()
        assert ingredients[index].type == type_, f"Ожидался тип {type_}, получен {ingredients[index].type}"

    @pytest.mark.parametrize("index, type_, name, price", expected_ingredients)
    def test_ingredients_have_expected_names(self, db, index, type_, name, price):
        ingredients = db.available_ingredients()
        assert ingredients[index].name == name, f"Ожидалось имя {name}, получено {ingredients[index].name}"

    @pytest.mark.parametrize("index, type_, name, price", expected_ingredients)
    def test_ingredients_have_expected_prices(self, db, index, type_, name, price):
        ingredients = db.available_ingredients()
        assert ingredients[index].price == price, f"Ожидалась цена {price}, получена {ingredients[index].price}"