from praktikum.bun import Bun


class TestBun:
    def test_get_name_bun(self):
        bun_name = Bun('Булочка Сладкая', 64.22)
        assert bun_name.get_name() == 'Булочка Сладкая'

    def test_get_price_bun(self):
        bun_price = Bun('Булочка Сладкая', 65.88)
        assert bun_price.get_price() == 65.88
