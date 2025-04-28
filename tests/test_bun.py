import pytest
from conftest import mock_bun
from mock_data import MockData
from src.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [
        (MockData.BLACK_BUN, MockData.BLACK_BUN_PRICE),
        (MockData.WHITE_BUN, MockData.WHITE_BUN_PRICE),
        (MockData.RED_BUN, MockData.RED_BUN_PRICE)
    ])
    def test_get_name_of_the_bun(self, name: str, price: int, mock_bun: Bun):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [
        (MockData.BLACK_BUN, MockData.BLACK_BUN_PRICE),
        (MockData.WHITE_BUN, MockData.WHITE_BUN_PRICE),
        (MockData.RED_BUN, MockData.RED_BUN_PRICE)
    ])
    def test_get_price_of_the_bun(self, name: str, price: int, mock_bun: Bun):
        bun = Bun(name, price)
        assert bun.get_price() == price