import pytest
from praktikum.bun import Bun
from tests.data import TestData


class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            (TestData.buns[0][0], TestData.buns[0][1]),
            (TestData.buns[1][0], TestData.buns[1][1]),
        ],
    )
    def test_get_name(self, name, price):

        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            (TestData.buns[0][0], TestData.buns[0][1]),
            (TestData.buns[1][0], TestData.buns[1][1]),
        ],
    )
    def test_get_price(self, name, price):

        bun = Bun(name, price)
        assert bun.get_price() == price

    def test_bun_initialization(self):

        name = "Тестовая булка"
        price = 150.5
        bun = Bun(name, price)

        assert bun.name == name
        assert bun.price == price
