class TestBun:

    def test_bun_initialization(self, bun):
        # тест корректности инициализации булочки
        assert bun.name == 'Краторная булка'
        assert bun.price == 125.50

    def test_bun_get_name(self, bun):
        # тест получения названия булочки
        assert bun.get_name() == 'Краторная булка'
        assert isinstance(bun.get_name(),str)

    def test_bun_get_price(self, bun):
        # тест получения цены булочки
        assert bun.get_price() == 125.50
        assert isinstance(bun.get_price(),float)