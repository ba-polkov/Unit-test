from ingredient_types import INGREDIENT_TYPE_FILLING
from tests.data import IngredientSauceData
from tests.data import IngredientFillingData


class TestIngredient:

    def test_ingredient_type(self, ingredient_filling):
        assert ingredient_filling.get_type() == INGREDIENT_TYPE_FILLING

    def test_ingredient_name(self, ingredient_sauce):
        assert ingredient_sauce.get_name() == IngredientSauceData.sauce_name

    def test_ingredient_price(self, ingredient_filling):
        assert ingredient_filling.get_price() == IngredientFillingData.filling_price
