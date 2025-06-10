from tests.conftest import mock_bun
from praktikum.burger import Burger

class TestBurger:

    def test_burger_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun