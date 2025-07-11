from praktikum.ingredient import Ingredient
from tests.test_data import SAUCE

class TestIngredient:
    def test_get_type(self):
        ing = Ingredient(SAUCE['type'], SAUCE['name'], SAUCE['price'])
        assert ing.get_type() == SAUCE['type']

    def test_get_name(self):
        ing = Ingredient(SAUCE['type'], SAUCE['name'], SAUCE['price'])
        assert ing.get_name() == SAUCE['name']

    def test_get_price(self):
        ing = Ingredient(SAUCE['type'], SAUCE['name'], SAUCE['price'])
        assert ing.get_price() == SAUCE['price']
