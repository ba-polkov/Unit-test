import pytest
from src.ingredient import Ingredient
from src.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from mock_data import MockData
from conftest import ingredient_sauce, ingredient_filling


class TestIngredient:

    @pytest.mark.parametrize('name, price', [
        (MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE),
        (MockData.SOUR_CREAM, MockData.SOUR_CREAM_PRICE),
        (MockData.CHILI_SAUCE, MockData.CHILI_SAUCE_PRICE)
    ])
    def test_get_price_of_the_sauce_price(self, ingredient_sauce: Ingredient, name, price):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert ingredient_sauce.get_price() == price

    @pytest.mark.parametrize('name, price', [
        (MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE),
        (MockData.SOUR_CREAM, MockData.SOUR_CREAM_PRICE),
        (MockData.CHILI_SAUCE, MockData.CHILI_SAUCE_PRICE)
    ])
    def test_get_name_of_the_sauce_name(self, ingredient_sauce: Ingredient, name, price):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert  ingredient_sauce.get_name() == name

    @pytest.mark.parametrize('name, price', [
        (MockData.HOT_SAUCE, MockData.HOT_SAUCE_PRICE),
        (MockData.SOUR_CREAM, MockData.SOUR_CREAM_PRICE),
        (MockData.CHILI_SAUCE, MockData.CHILI_SAUCE_PRICE)
    ])
    def test_get_type_of_the_sauce_type(self, ingredient_sauce: Ingredient, name, price):
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert ingredient_sauce.get_type() == INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize('name, price', [
        (MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE),
        (MockData.DINOSAUR_FILLING, MockData.DINOSAUR_FILLING_PRICE),
        (MockData.SAUSAGE_FILLING, MockData.SAUSAGE_FILLING_PRICE)
    ])
    def test_get_price_of_the_filling_price(self, ingredient_filling: Ingredient, name, price):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, name, price)
        assert ingredient_filling.get_price() == price

    @pytest.mark.parametrize('name, price', [
        (MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE),
        (MockData.DINOSAUR_FILLING, MockData.DINOSAUR_FILLING_PRICE),
        (MockData.SAUSAGE_FILLING, MockData.SAUSAGE_FILLING_PRICE)
    ])
    def test_get_name_of_the_filling_name(self, ingredient_filling: Ingredient, name, price):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, name, price)
        assert ingredient_filling.get_name() == name

    @pytest.mark.parametrize('name, price', [
        (MockData.CUTLET_FILLING, MockData.CUTLET_FILLING_PRICE),
        (MockData.DINOSAUR_FILLING, MockData.DINOSAUR_FILLING_PRICE),
        (MockData.SAUSAGE_FILLING, MockData.SAUSAGE_FILLING_PRICE)
    ])
    def test_get_type_of_the_filling_type(self, ingredient_filling: Ingredient, name, price):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, name, price)
        assert ingredient_filling.get_type() == INGREDIENT_TYPE_FILLING