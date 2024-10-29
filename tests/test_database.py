import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestDataBase:
    def test_available_buns(database):
        buns = database.available_buns()
        assert isinstance(buns, list), "Метод available_buns() должен возвращать список"
        assert all(isinstance(bun, Bun) for bun in buns), "Все элементы списка должны быть экземплярами Bun"
        assert len(buns) > 0, "Список булочек не должен быть пустым"


    def test_available_ingredients(database):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list), "Метод available_ingredients() должен возвращать список"
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients), "Все элементы списка должны быть экземплярами Ingredient"
        assert len(ingredients) > 0, "Список ингредиентов не должен быть пустым"


    def test_database_buns_content(database):
        buns = database.available_buns()
        expected_bun_names = ["black bun", "white bun", "red bun"]
        actual_bun_names = [bun.get_name() for bun in buns]
        assert actual_bun_names == expected_bun_names, "Список булочек не соответствует ожидаемому"


    def test_database_ingredients_content(database):
        ingredients = database.available_ingredients()
        expected_ingredient_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        actual_ingredient_names = [ingredient.get_name() for ingredient in ingredients]
        assert actual_ingredient_names == expected_ingredient_names, "Список ингредиентов не соответствует ожидаемому"


    def test_database_with_mocked_buns(mocker, database):
        mocked_buns = [Bun("Моковая булочка", 0.0)]
        mocker.patch.object(database, 'available_buns', return_value=mocked_buns)
        buns = database.available_buns()
        assert buns == mocked_buns, "Метод available_buns() должен вернуть замоканный список булочек"


    def test_database_with_mocked_ingredients(mocker, database):
        mocked_ingredients = [Ingredient("SAUCE", "Моковый соус", 0.0)]
        mocker.patch.object(database, 'available_ingredients', return_value=mocked_ingredients)
        ingredients = database.available_ingredients()
        assert ingredients == mocked_ingredients, "Метод available_ingredients() должен вернуть замоканный список ингредиентов"
