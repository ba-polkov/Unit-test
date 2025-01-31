from praktikum.ingredient import Ingredient
from data import Data
import allure


class TestBun:
    @allure.title('Проверка инициализации ingredient_type, name, price')
    def test_initial_name_price(self):
        ing = Ingredient(Data.sauce_type, Data.sauce_name, Data.sauce_price)
        assert ing.type == Data.sauce_type
        assert ing.name == Data.sauce_name
        assert ing.price == Data.sauce_price

    @allure.title('Проверка метода get_name, возвращающего name ингредиента')
    def test_get_ingredient_name(self):
        ing = Ingredient(Data.sauce_type, Data.sauce_name, Data.sauce_price)
        assert ing.name == ing.get_name()

    @allure.title('Проверка метода get_price, возвращающего price ингредиента')
    def test_get_ingredient_price(self):
        ing = Ingredient(Data.sauce_type, Data.sauce_name, Data.sauce_price)
        assert ing.price == ing.get_price()

    @allure.title('Проверка метода get_name, возвращающего name ингредиента')
    def test_get_ingredient_type(self):
        ing = Ingredient(Data.sauce_type, Data.sauce_name, Data.sauce_price)
        assert ing.type == ing.get_type()
