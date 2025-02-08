from bun import Bun
from tests.data import BunData


class TestBun:


# Тест для проверки метода get_name
    def test_get_name(self, default_bun):
        assert default_bun.get_name() == BunData.bun_name

# Тест для проверки метода get_price
    def test_get_price(self, default_bun):
        assert default_bun.get_price() == BunData.bun_price

# Тест для проверки инициализации с нулевой ценой
    def test_zero_price(self):
        bun = Bun("Булочка с маком", 0.0)
        assert bun.get_price() == 0.0
