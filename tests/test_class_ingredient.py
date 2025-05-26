import allure

from praktikum.ingredient import Ingredient
from data_for_test import TestIngredientsData as TID

class TestClassIngredient:
    @allure.title('Возвращение нужного название ингредиента')
    def test_return_ingredient_name(self):
        ingredient_name = Ingredient(**TID.INGREDIENT).get_name()
        assert ingredient_name == TID.INGREDIENT['name']

    @allure.title('Возвращение нужной стоимости ингредиента')
    def test_return_ingredient_price(self):
        ingredient_price = Ingredient(**TID.INGREDIENT).get_price()
        assert ingredient_price == TID.INGREDIENT['price']

    @allure.title('Возвращение нужного типа ингредиента')
    def test_return_ingredient_type(self):
        ingredient_type = Ingredient(**TID.INGREDIENT).get_type()
        assert ingredient_type == TID.INGREDIENT['ingredient_type']

    @allure.title('Возвращение нужного типа названия ингредиента')
    def test_return_valid_ingredient_name_type(self):
        ingredient_name = Ingredient(**TID.INGREDIENT).name
        assert isinstance(ingredient_name, str)

    @allure.title('Возвращение нужного типа стоимости ингредиента')
    def test_return_valid_ingredient_price_type(self):
        ingredient_price = Ingredient(**TID.INGREDIENT).price
        assert isinstance(ingredient_price, int)

    @allure.title('Возвращение нужного типа данных типа ингредиента')
    def test_return_valid_type_ingredient_type(self):
        ingredient_type = Ingredient(**TID.INGREDIENT).type
        assert isinstance(ingredient_type, str)