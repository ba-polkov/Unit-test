from praktikum.bun import Bun


class TestBun:
    def test_name_of_bun_true(self):
        bun = Bun("Кунжутная", 100.99)
        assert bun.name == "Кунжутная"
        assert isinstance(bun.name, str)


    def test_price_of_bun_true(self):
        bun = Bun("Кунжутная", 100.99)
        assert bun.price == 100.99
        assert isinstance(bun.price, float)


    def test_get_name_true(self):
        bun = Bun("Кунжутная", 100.99)
        assert bun.get_name() == "Кунжутная"
        assert isinstance(bun.get_name(), str)


    def test_get_price_true(self):
        bun = Bun("Кунжутная", 100.99)
        assert bun.get_price() == 100.99
        assert isinstance(bun.get_price(), float)
