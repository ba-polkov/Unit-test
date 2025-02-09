from praktikum.bun import Bun


class TestBun:
    def test_get_name_shows_correct_bun_name(self):
        buns = Bun("funky", 99)
        actual_result = buns.get_name()
        print(actual_result)
        assert actual_result

    def test_get_price_shows_correct_bun_price(self):
        buns = Bun("funky", 99)
        actual_result = buns.get_price()
        print(actual_result)
        assert actual_result
