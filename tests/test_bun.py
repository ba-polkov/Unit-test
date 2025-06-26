from conftest import *


class TestBun:


    def test_get_name_bun(self, mock_bun1):
        assert mock_bun1.get_name() == Burger1.bun_name


    def test_get_price_bun(self, mock_bun2):
        assert mock_bun2.get_price() == Burger2.bun_price