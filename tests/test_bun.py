from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun_name = 'Люкс'
        bun = Bun(bun_name, 7.50)
        assert bun_name == bun.get_name()

    def test_get_price(self):
        bun_price = 7.50
        bun = Bun('Тарли', bun_price)
        assert bun_price == bun.get_price()
