import pytest
from Diplom_1.praktikum.database import Database
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient
from Diplom_1.praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.fixture
    def database(self):
        """
        Фикстура для создания экземпляра Database.
        """
        return Database()

    def test_available_buns(self, database):
        """
        Проверяем, что метод available_buns возвращает корректный список булочек.
        """
        buns = database.available_buns()

        # Проверяем количество булочек
        assert len(buns) == 3

        # Проверяем, что каждая булочка имеет правильное имя и цену
        assert isinstance(buns[0], Bun)
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100

        assert isinstance(buns[1], Bun)
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200

        assert isinstance(buns[2], Bun)
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    def test_available_ingredients(self, database):
        """
        Проверяем, что метод available_ingredients возвращает корректный список ингредиентов.
        """
        ingredients = database.available_ingredients()

        # Проверяем количество ингредиентов
        assert len(ingredients) == 6

        # Проверяем, что каждый ингредиент имеет правильный тип, имя и цену
        assert isinstance(ingredients[0], Ingredient)
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100

        assert isinstance(ingredients[1], Ingredient)
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200

        assert isinstance(ingredients[2], Ingredient)
        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_price() == 300

        assert isinstance(ingredients[3], Ingredient)
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100

        assert isinstance(ingredients[4], Ingredient)
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200

        assert isinstance(ingredients[5], Ingredient)
        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_price() == 300