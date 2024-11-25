from src.bun import Bun


class TestBun:

    def test_bun_initialization(self):
        bun = Bun("black bun", 100.21)
        assert bun.name == "black bun"
        assert bun.price == 100.21

    def test_bun_get_name(self):
        bun = Bun("black bun", 100.21)
        assert bun.get_name() == "black bun"

    def test_bun_get_price(self):
        bun = Bun("black bun", 100.21)
        assert bun.get_price() == 100.21

    def test_bun_price_is_float(self):
        bun = Bun("black bun", 100.21)
        assert isinstance(bun.price, float)
