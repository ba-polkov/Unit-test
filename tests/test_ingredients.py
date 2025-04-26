from data import *

class TestIngredient:

    def test_get_name_sauce_success(self, mock_sauce):
        expected_name = mock_sauce.get_name()
        assert expected_name in [sauce[1] for sauce in Ingredients.sauces]

    def test_get_name_filling_success(self, mock_filling):
        expected_name = mock_filling.get_name()
        assert expected_name in [filling[1] for filling in Ingredients.fillings]

    def test_get_price_sauce_success(self, mock_sauce):
        expected_price = mock_sauce.get_price()
        assert expected_price in [sauce[2] for sauce in Ingredients.sauces]

    def test_get_price_filling_success(self, mock_filling):
        expected_price = mock_filling.get_price()
        assert expected_price in [filling[2] for filling in Ingredients.fillings]

    def test_get_type_sauce_success(self, mock_sauce):
        expected_type = mock_sauce.get_type()
        assert expected_type == INGREDIENT_TYPE_SAUCE

    def test_get_type_filling_success(self, mock_filling):
        expected_type = mock_filling.get_type()
        assert expected_type == INGREDIENT_TYPE_FILLING