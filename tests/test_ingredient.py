from data import BurgerData
import pytest




class TestIngredient:

    @pytest.mark.parametrize(
        'field_to_check, expected_result, expected_type',
        [
            ('name', 'hot sauce', str),
            ('type', 'SAUCE', str),
            ('price', 15.00, float)
        ])
    def test_ingredient_initialization(self, ingredient, field_to_check, expected_result, expected_type):
        actual_value = getattr(ingredient, field_to_check)
        assert actual_value == expected_result and isinstance(actual_value, expected_type)

    def test_get_type_ingredients(self, ingredient):
        actual_value = ingredient.get_type()
        assert actual_value == BurgerData.SAUCES_TYPE and isinstance(actual_value, str)

    def test_get_name_ingredients(self, ingredient):
        actual_value = ingredient.get_name()
        assert actual_value == BurgerData.SAUCES_NAME and isinstance(actual_value, str)

    def test_get_price_ingredients(self, ingredient):
        actual_value = ingredient.get_price()
        assert actual_value == BurgerData.SAUCES_PRICE and isinstance(actual_value, float)
