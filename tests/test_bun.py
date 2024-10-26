import pytest
from yandex.bun import Bun
from data import Buns


class TestBun:

    @pytest.mark.parametrize('name, price',
                             [
                                 (Buns.bun_name_1, Buns.bun_price_1),
                                 (Buns.bun_name_2, Buns.bun_price_2)
                             ]
                            )
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price',
                             [
                                 (Buns.bun_name_1, Buns.bun_price_1),
                                 (Buns.bun_name_2, Buns.bun_price_2)
                             ]
                            )
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
