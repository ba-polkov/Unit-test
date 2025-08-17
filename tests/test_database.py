import allure
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @allure.title('Получение доступных булочек')
    def test_available_buns(self, db, bun_data):
        buns = db.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == bun_data['name']
        assert buns[0].get_price() == bun_data['price']

    @allure.title('Получение доступных ингредиентов')
    def test_available_ingredients(self, db, ingredient_data):
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(sauces) == 3
        assert len(fillings) == 3

        assert sauces[0].get_name() == ingredient_data['sauce']['name']
        assert fillings[0].get_name() == ingredient_data['filling']['name']