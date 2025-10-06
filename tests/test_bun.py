import pytest

from praktikum.bun import Bun
from src.data import BUNS_DATA, BUNS_WITH_NEGATIVE_PRICES


class TestBun:
    # Проверка инициализации булочки
    def test_bun_init_sets_name_and_price_correctly(self):
        name, price = BUNS_DATA[0]
        bun = Bun(name, price)
        assert bun.name == name, f"Ожидалось имя булочки '{name}', получено '{bun.name}'"
        assert bun.price == price, f"Ожидалась цена булочки '{price}', получена '{bun.price}'"

    # Проверка геттеров
    @pytest.mark.parametrize("name, price", BUNS_DATA)
    def test_bun_get_name_returns_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name, f"Ожидалось имя булочки '{expected_name}', получено '{bun.name}'"

    @pytest.mark.parametrize("name, price", BUNS_DATA)
    def test_bun_get_price_returns_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price, f"Ожидалась цена булочки '{expected_price}', получена '{bun.price}'"

    # Проверка отрицательных цен
    @pytest.mark.parametrize("name, price", BUNS_WITH_NEGATIVE_PRICES)
    @pytest.mark.xfail(reason = 'Negative price should raise ValueError, but not implemented - this is a bug')
    def test_bun_with_negative_price_raises_value_error(self, name, price):
        # Проверка на исключение при отрицательной цене
        with pytest.raises(ValueError, match="Цена булочки не может быть отрицательной"):
            Bun(name, price)
