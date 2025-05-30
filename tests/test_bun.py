from bun import Bun


class TestBun:

    def test_get_name(self):
        name = 'test'
        price = 99.9
        bun = Bun(name, price)

        assert bun.get_name() == name


    def test_get_price(self):
        name = 'test'
        price = 99.9
        bun = Bun(name, price)

        assert bun.get_price() == price
