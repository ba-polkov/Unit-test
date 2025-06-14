from conftest import *


class TestIngredient:

    def test_get_type_filling(self, mock_filling1):
        assert mock_filling1.get_type() == Burger1.filling_type


    def test_get_name_filling(self, mock_filling1):
        assert mock_filling1.get_name() == Burger1.filling_name


    def test_get_price_filling(self, mock_filling2):
        assert mock_filling2.get_price() == Burger2.filling_price


    def test_get_type_sauce(self, mock_sauce1):
        assert mock_sauce1.get_type() == Burger1.sauce_type


    def test_get_name_sauce(self, mock_sauce1):
        assert mock_sauce1.get_name() == Burger1.sauce_name


    def test_get_price_sauce(self, mock_sauce2):
        assert mock_sauce2.get_price() == Burger2.sauce_price