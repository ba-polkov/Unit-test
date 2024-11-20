import allure
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT2_NAME, INGREDIENT2_PRICE

class TestIngredient:
    @allure.title("Проверка инициализации ингредиента типа начинка")
    def test_create_ingredient_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT2_NAME, INGREDIENT2_PRICE)
        assert ingredient.type == INGREDIENT_TYPE_FILLING
        assert ingredient.name == INGREDIENT2_NAME
        assert ingredient.price == INGREDIENT2_PRICE

    @allure.title("Проверка инициализации ингредиента типа соус")
    def test_create_ingredient_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == INGREDIENT_NAME
        assert ingredient.price == INGREDIENT_PRICE

    @allure.title("Узнать цену начинки")
    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT2_NAME, INGREDIENT2_PRICE)
        assert ingredient.get_price() == INGREDIENT2_PRICE

    @allure.title("Узнать название соуса")
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        assert ingredient.get_name() == INGREDIENT_NAME

    @allure.title("Узнать тип ингредиента")
    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
