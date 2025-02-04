from praktikum.bun import Bun


class TestBun:
    def test_bun_get_name_return_name(self):
        bun = Bun('bun_name', 3)
        assert bun.get_name() == 'bun_name', f'Expected \'bun_name\' but got {bun.get_name()}'

    def test_bun_get_price_return_price(self):
        bun = Bun('bun_name', 3)
        assert bun.get_price() == 3, f'Expected \'3\' but got {bun.get_price()}'
