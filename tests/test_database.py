import pytest
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import allure


class TestDatabase:
    @allure.title("Проверка доступных булочек")
    def test_available_buns_returns_list_of_buns(self):
        database = Database()
        with allure.step("Получить список доступных булочек"):
            buns = database.available_buns()

        with allure.step("Проверить тип возвращаемого значения"):
            assert isinstance(buns, list)
            assert all(isinstance(bun, Bun) for bun in buns)

        with allure.step("Проверить количество булочек"):
            assert len(buns) == 3

    @allure.title("Проверка корректности данных булочек")
    def test_available_buns_contains_correct_buns(self):
        database = Database()
        with allure.step("Получить список булочек"):
            buns = database.available_buns()

        with allure.step("Подготовить ожидаемые данные"):
            expected_data = [
                ("black bun", 100),
                ("white bun", 200),
                ("red bun", 300)
            ]

        with allure.step("Сверить фактические данные с ожидаемыми"):
            for i, (expected_name, expected_price) in enumerate(expected_data):
                with allure.step(f"Проверка булочки {i + 1}"):
                    assert buns[i].get_name() == expected_name
                    assert buns[i].get_price() == expected_price

    @allure.title("Проверка доступных ингредиентов")
    def test_available_ingredients_returns_list_of_ingredients(self):
        database = Database()
        with allure.step("Получить список ингредиентов"):
            ingredients = database.available_ingredients()

        with allure.step("Проверить тип возвращаемого значения"):
            assert isinstance(ingredients, list)
            assert all(isinstance(ing, Ingredient) for ing in ingredients)

        with allure.step("Проверить общее количество ингредиентов"):
            assert len(ingredients) == 6

    @allure.title("Проверка корректности данных соусов")
    def test_available_ingredients_contains_correct_sauces(self):
        database = Database()
        with allure.step("Получить и отфильтровать соусы"):
            sauces = [
                ing for ing in database.available_ingredients()
                if ing.get_type() == INGREDIENT_TYPE_SAUCE
            ]

        with allure.step("Подготовить эталонные данные"):
            expected_sauces = [
                ("hot sauce", 100),
                ("sour cream", 200),
                ("chili sauce", 300)
            ]

        with allure.step("Проверить соусы"):
            assert len(sauces) == 3
            for i, (expected_name, expected_price) in enumerate(expected_sauces):
                with allure.step(f"Проверка соуса {i + 1}"):
                    assert sauces[i].get_name() == expected_name
                    assert sauces[i].get_price() == expected_price

    @allure.title("Проверка корректности данных начинок")
    def test_available_ingredients_contains_correct_fillings(self):
        database = Database()
        with allure.step("Получить и отфильтровать начинки"):
            fillings = [
                ing for ing in database.available_ingredients()
                if ing.get_type() == INGREDIENT_TYPE_FILLING
            ]

        with allure.step("Подготовить эталонные данные"):
            expected_fillings = [
                ("cutlet", 100),
                ("dinosaur", 200),
                ("sausage", 300)
            ]

        with allure.step("Проверить начинки"):
            assert len(fillings) == 3
            for i, (expected_name, expected_price) in enumerate(expected_fillings):
                with allure.step(f"Проверка начинки {i + 1}"):
                    assert fillings[i].get_name() == expected_name
                    assert fillings[i].get_price() == expected_price
