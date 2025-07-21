import pytest
from typing import List
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    database = Database()

    # Тест на проверку количества булочек
    def test_count_available_buns(self):
        buns = self.database.available_buns()
        assert len(buns) == 3

    # Тест на проверку количества ингредиентов
    def test_count_available_ingredients(self):
        assert len(self.database.available_ingredients()) == 6

    # Тест на проверку количества соусов
    def test_count_available_sauces(self):
        ingredients = self.database.available_ingredients()
        sauces = [ingredient for ingredient in ingredients if ingredient.type == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    # Тест на проверку количества начинок
    def test_count_available_fillings(self):
        ingredients = self.database.available_ingredients()
        fillings = [ingredient for ingredient in ingredients if ingredient.type == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    # Тест на проверку данных булочек
    @pytest.mark.parametrize('index,expected_name,expected_price', [
        (0, 'black bun', 100),
        (1, 'white bun', 200),
        (2, 'red bun', 300)
        ])
    def test_correct_data_buns(self, index, expected_name, expected_price):
        buns = self.database.available_buns()
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    # Тест на проверку данных ингредиентов
    @pytest.mark.parametrize('index,expected_type,expected_name,expected_price',[
            (0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
            (2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
            (3, INGREDIENT_TYPE_FILLING, 'cutlet', 100),
            (4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
            (5, INGREDIENT_TYPE_FILLING, 'sausage', 300),
            ])
    def test_correct_data_ingredients(self, index, expected_type, expected_name, expected_price):
        ingredients = self.database.available_ingredients()
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price

    # Тест на проверку возвращения списка булочек
    def test_returns_list_available_buns(self):
        assert isinstance(self.database.available_buns(), List)

    # Тест на проверку возвращения списка ингредиентов
    def test_returns_list_available_ingredients(self):
        assert isinstance(self.database.available_ingredients(), List)