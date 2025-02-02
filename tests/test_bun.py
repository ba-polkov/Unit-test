from praktikum.bun import Bun

# Тестируем булочки
class TestsClassBun:
    # Тест получения имени булочки
    def test_get_name_create_bun_get_name_bun(self):
        bun = Bun('Краторная булка №-200i', 1255)
        assert bun.get_name() == 'Краторная булка №-200i'

    # Тест получения цены булочки
    def test_get_price_create_bun_get_price_bun(self):
        bun = Bun('Краторная булка №-200i', 1255)
        assert bun.get_price() == 1255

