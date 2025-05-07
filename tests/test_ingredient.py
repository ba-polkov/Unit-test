import pytest
import allure
from praktikum.ingredient import Ingredient


@allure.feature("Ингредиент")
@allure.story("Основные методы ингредиента")
class TestIngredient:

    @allure.title("Проверка метода get_price")
    def test_ingredient_get_price(self):
        with allure.step("Создаем ингредиент с ценой 50.0"):
            ingredient = Ingredient("SAUCE", "BBQ", 50.0)

        with allure.step("Проверка, что метод get_price возвращает правильную цену"):
            assert ingredient.get_price() == 50.0, "Метод get_price должен возвращать цену ингредиента"

    @allure.title("Проверка метода get_name")
    def test_ingredient_get_name(self):
        with allure.step("Создаем ингредиент с именем 'Bacon'"):
            ingredient = Ingredient("FILLING", "Bacon", 70.0)

        with allure.step("Проверка, что метод get_name возвращает правильное имя"):
            assert ingredient.get_name() == "Bacon", "Метод get_name должен возвращать имя ингредиента"

    @allure.title("Проверка метода get_type")
    def test_ingredient_get_type(self):
        with allure.step("Создаем ингредиент с типом 'SAUCE'"):
            ingredient = Ingredient("SAUCE", "Ketchup", 30.0)

        with allure.step("Проверка, что метод get_type возвращает правильный тип"):
            assert ingredient.get_type() == "SAUCE", "Метод get_type должен возвращать тип ингредиента"