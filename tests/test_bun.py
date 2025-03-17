from praktikum.bun import Bun
from data import BunData
import pytest


class TestBun:

    def test_get_name(self):
        bun_obj = Bun(BunData.bun_name, BunData.bun_price)
        assert bun_obj.get_name() == BunData.bun_name

    def test_get_price(self):
        bun_obj = Bun(BunData.bun_name, BunData.bun_price)
        assert bun_obj.get_price() == BunData.bun_price

    @pytest.mark.skip(reason="Валидация данных в классе не реализована.")
    @pytest.mark.parametrize('bun_name, bun_price', [[123, 2.55], ['Крафтовая булка', '2,55']])
    def test_invalid_params_type_shows_type_error(self, bun_name, bun_price):
        with pytest.raises(TypeError):
            Bun(bun_name, bun_price)

    @pytest.mark.skip(reason="Валидация данных в классе не реализована.")
    @pytest.mark.parametrize('bun_name, bun_price', [['', 2.55], ['Крафтовая булка', 0], ['Крафтовая булка', -5.55]])
    def test_incorrect_params_shows_value_error(self, bun_name, bun_price):
        with pytest.raises(ValueError):
            Bun(bun_name, bun_price)
