from praktikum.ingredient_types import *
import allure


class TestIngredientTypes:
    @allure.title('Проверка значений INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING')
    def test_ingredient_types(self):
        assert INGREDIENT_TYPE_SAUCE == 'SAUCE'
        assert INGREDIENT_TYPE_FILLING == 'FILLING'
