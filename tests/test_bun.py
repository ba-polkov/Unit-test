from praktikum.bun import Bun

class TestBun:

    def test_get_name_success(self):
        bun = Bun("Багет", 50)
        assert bun.get_name() == "Багет"


    def test_get_price_success(self):
        bun = Bun("Багет", 50)
        assert bun.get_price() == 50