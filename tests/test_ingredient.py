from praktikum.ingredient import Ingredient
from data import Data
import allure


class TestBun:
    @allure.title("Проверить инициализацию типа ингредиента, названия и цены")
    def test_initial_name_price(self):
        ing = Ingredient(Data.sauce_type, Data.sauce_name, Data.sauce_price)
        assert (
            ing.type == Data.sauce_type
            and ing.name == Data.sauce_name
            and ing.price == Data.sauce_price
        )

    @allure.title("Проверить метод get_name, выдающий название ингредиента")
    def test_get_ingredient_name(self):
        ing = Ingredient(Data.sauce_type, Data.sauce_name, Data.sauce_price)
        assert ing.name == ing.get_name()

    @allure.title("Проверить метод get_price, выдающий цену ингредиента")
    def test_get_ingredient_price(self):
        ing = Ingredient(Data.sauce_type, Data.sauce_name, Data.sauce_price)
        assert ing.price == ing.get_price()

    @allure.title("Проверить метод get_name, выдающий название ингредиента")
    def test_get_ingredient_type(self):
        ing = Ingredient(Data.sauce_type, Data.sauce_name, Data.sauce_price)
        assert ing.type == ing.get_type()
