from praktikum.bun import Bun


class TestBun:
    def test_get_name_returns_name(self):
        bun = Bun('Бутафория', 60.0)
        result = bun.get_name()

        assert result == 'Бутафория', f'Ожидалось "Бутафория", получили {result}'

    def test_get_price_returns_price(self):
        bun = Bun('Биг Спешиал', 120.0)
        result = bun.get_price()

        assert result == 120.0, f'Ожидалось "120.0", получили {result}'
