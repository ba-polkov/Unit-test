from praktikum.bun import Bun


class TestBun:

    def test_get_name_get_right_name(self):
        bun = Bun('name', 1.1)
        assert bun.get_name() == 'name'

    def test_get_name_get_right_price(self):
        bun = Bun('name', 1.1)
        assert bun.get_price() == 1.1