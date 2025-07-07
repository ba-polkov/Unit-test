
from typing import List

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    # Тест на проверку количества булочек
    def test_count_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    # Тест на проверку количества ингредиентов
    def test_count_available_ingredients(self, database):
        assert len(database.available_ingredients()) == 6

    # Тест на проверку количества соусов
    def test_initial_sauces_count(self, database):
        ingredients = database.available_ingredients()
        sauces = [ingredient for ingredient in ingredients if ingredient.type == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    # Тест на проверку количества начинок
    def test_initial_toppings_count(self, database):
        ingredients = database.available_ingredients()
        fillings = [ingredient for ingredient in ingredients if ingredient.type == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    # Тест на проверку данных булочек
    def test_correct_data_buns(self, database):
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun" and buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun" and buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun" and buns[2].get_price() == 300

    # Тест на проверку данных ингредиентов
    def test_correct_data_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce" and ingredients[0].get_price() == 100
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == "sour cream" and ingredients[1].get_price() == 200
        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_name() == "chili sauce" and ingredients[2].get_price() == 300
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == "cutlet" and ingredients[3].get_price() == 100
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == "dinosaur" and ingredients[4].get_price() == 200
        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_name() == "sausage" and ingredients[5].get_price() == 300

    # Тест на проверку возвращения списка булочек
    def test_returns_list_available_buns(self, database):
        assert isinstance(database.available_buns(), List)

    # Тест на проверку возвращения списка ингредиентов
    def test_returns_list_available_ingredients(self, database):
        assert isinstance(database.available_ingredients(), List)