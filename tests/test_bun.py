import pytest
from data import BurgerData


class TestBun:

    @pytest.mark.parametrize(
        'field_to_check, expected_result, expected_type',
        [
            ('name', 'black bun', str),
            ('price', 10.00, float)
        ])
    def test_bun_initialization(self, bun, field_to_check, expected_result, expected_type):
        actual_value = getattr(bun, field_to_check)
        assert actual_value == expected_result and isinstance(actual_value, expected_type)

    def test_bun_name(self, bun):
        actual_value = bun.get_name()
        assert actual_value == BurgerData.BUNS_NAME and isinstance(actual_value, str)

    def test_bun_price(self, bun):
        actual_value = bun.get_price()
        assert actual_value == BurgerData.BUNS_PRICE and isinstance(actual_value, float)
