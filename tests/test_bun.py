import data


class TestBun:
    def test_get_name_bun_one_bun_valid_name(self, bun):
        assert bun.name == data.BUN_NAME_COSMOBUN

    def test_get_price_bun_one_bun_valid_price(self, bun):
        assert bun.price == data.BUN_PRICE_COSMOBUN