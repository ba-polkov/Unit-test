import pytest

import data
from praktikum.bun import Bun
from conftest import mock_bun


class TestBun():

    @pytest.mark.parametrize(
       'name, price, is_param',
        [[data.DEF_BUN_NAME, data.DEF_BUN_PRICE, "name"],
         [data.DEF_BUN_NAME, data.DEF_BUN_PRICE, "price"]]
    )
    def test_get_mame_and_price_positive_value(self, mock_bun, name, price, is_param):
        testbun = Bun(mock_bun.name, mock_bun.price)
        if is_param == "name":
            assert testbun.get_name() == name, "Не корректный метод get_name"
        else:
            assert testbun.get_price() == price, "Не корректный метод get_price"
