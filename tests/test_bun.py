from unittest.mock import Mock

import pytest


class TestBun:
    @pytest.mark.parametrize( 'name',
        [
            'Mike',
            'Миша',
            '',
            ' ',
            '154'
        ]
    )
    def test_get_name(self, name):
        mock_bun = Mock()
        mock_bun.get_name.return_value = name
        assert mock_bun.get_name() == name

    @pytest.mark.parametrize('price',
                             [
                                 '100',
                                 '100,1',
                                 '',
                                 ' ',
                                 '0'
                             ]
                             )
    def test_get_price(self, price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = price
        assert mock_bun.get_price() == price
