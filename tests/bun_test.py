from praktikum.bun import Bun

class TestBun:

    def test_get_name(self):
        bun = Bun("Ржаная", 15)
        assert bun.get_name() == bun.name

    def test_get_price(self):
        bun = Bun("Ржаная", 15)
        assert bun.get_price() == bun.price

