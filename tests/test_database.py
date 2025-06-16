import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import DataDatabase


class TestDatabase:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.database = Database()

    @pytest.mark.parametrize('index, expected_name, expected_price', DataDatabase.BUN_TEST_DATA)
    def test_available_buns_returns_correct_items(self, index, expected_name, expected_price):
        """Проверка корректности элементов списка булочек."""
        buns = self.database.available_buns()
        bun = buns[index]

        assert bun.name == expected_name
        assert bun.price == expected_price

    def test_available_buns_returns_bun_objects(self):
        """Проверка, что available_buns() возвращает объекты класса Bun."""
        buns = self.database.available_buns()

        for bun in buns:
            assert isinstance(bun, Bun)

    @pytest.mark.parametrize('index, expected_type, expected_name, expected_price', DataDatabase.INGREDIENT_TEST_DATA)
    def test_available_ingredients_returns_correct_items(self, index, expected_type, expected_name, expected_price):
        """Проверка корректности элементов списка ингредиентов."""
        ingredients = self.database.available_ingredients()
        ingredient = ingredients[index]

        assert ingredient.type == expected_type
        assert ingredient.name == expected_name
        assert ingredient.price == expected_price

    def test_available_ingredients_returns_ingredient_objects(self):
        """Проверка, что available_ingredients() возвращает объекты класса Ingredient."""
        ingredients = self.database.available_ingredients()

        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)

    def test_available_buns_returns_same_list_instance(self):
        """Проверка, что available_buns() возвращает тот же экземпляр списка."""
        buns1 = self.database.available_buns()
        buns2 = self.database.available_buns()

        assert buns1 is buns2
        assert buns1 == buns2

    def test_available_ingredients_returns_same_list_instance(self):
        """Проверка, что available_ingredients() возвращает тот же экземпляр списка."""
        ingredients1 = self.database.available_ingredients()
        ingredients2 = self.database.available_ingredients()

        # Проверяем, что это один и тот же объект в памяти
        assert ingredients1 is ingredients2
        # Проверяем, что содержимое идентично
        assert ingredients1 == ingredients2