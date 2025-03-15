from praktikum.bun import Bun
import pytest


class TestBun:
    bun_name = 'Крафтовая булка'
    bun_price = 2.55

    def test_get_name(self):
        bun_obj = Bun(self.bun_name, self.bun_price)
        assert bun_obj.get_name() == self.bun_name

    def test_get_price(self):
        bun_obj = Bun(self.bun_name, self.bun_price)
        assert bun_obj.get_price() == self.bun_price

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
