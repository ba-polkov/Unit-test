import allure

from ingredient import Ingredient
from data import BurgerConsist as bc

class TestIngredient:

# тест для метода get_price
    @allure.title('проверка получения стоимости ингредиента')
    def test_get_price(self):
            sauce = Ingredient(bc.INGREDIENT_TYPE_SAUCE, bc.INGREDIENT_TYPE_SAUCE_NAME, bc.SAUCE_PRICE)
            assert sauce.get_price() == bc.SAUCE_PRICE

# тест для метода get_name
    @allure.title('проверка получения  имени ингредиента')
    def test_get_name(self):
            sauce = Ingredient(bc.INGREDIENT_TYPE_SAUCE, bc.INGREDIENT_TYPE_SAUCE_NAME, bc.SAUCE_PRICE)
            assert sauce.get_name() == bc.INGREDIENT_TYPE_SAUCE_NAME

# тест для метода get_type
    @allure.title('проверка получения  типа ингредиента')
    def test_get_type(self):
            sauce = Ingredient(bc.INGREDIENT_TYPE_SAUCE, bc.INGREDIENT_TYPE_SAUCE_NAME, bc.SAUCE_PRICE)
            assert sauce.get_type() == bc.INGREDIENT_TYPE_SAUCE


