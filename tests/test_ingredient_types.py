from praktikum.ingredient_types import *
import allure


class TestIngredientTypes:
    @allure.title("Проверить значения INGREDIENT_TYPE_SAUCE и INGREDIENT_TYPE_FILLING")
    def test_ingredient_types(self):
        assert INGREDIENT_TYPE_SAUCE == "SAUCE" and INGREDIENT_TYPE_FILLING == "FILLING"
