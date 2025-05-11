from unittest.mock import Mock

import pytest
import data


class TestBun:
    @pytest.mark.parametrize( 'name', data.DATA_TEST_BUN_NAME)
    def test_get_name(self, name):
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        assert mock_bun.get_name() == name

    @pytest.mark.parametrize('price', data.DATA_TEST_BUN_PRICE)
    def test_get_price(self, price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = price
        assert mock_bun.get_price() == price
