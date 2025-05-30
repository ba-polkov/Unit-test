from praktikum.bun import Bun

class TestBun:

    # Тест на успешное создание новой булки
    def test_new_bun(self):
        bun = Bun("Булка смерти", 405)
        assert bun.get_name() == "Булка смерти"
        assert bun.get_price() == 405