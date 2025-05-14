import pytest
from Diplom_1.bun import Bun
from Diplom_1.database import Database

class TestBun:
    @pytest.fixture
    def database(self):
        """
        Фикстура для создания экземпляра Database.
        """
        return Database()

    @pytest.fixture
    def bun(self):
        """
        Фикстура для создания экземпляра Bun (по умолчанию).
        """
        return Bun("default bun", 0)  # Создаем Bun с какими-то значениями по умолчанию


    @pytest.mark.parametrize(
        "bun_name, bun_price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ],
    )
    def test_get_name_parametrize(self, database, bun_name, bun_price):
        """
        Проверяет правильность работы метода get_name().
        """
        buns = database.available_buns()
        found_bun = None
        for bun in buns:
            if bun.name == bun_name:
                found_bun = bun
                break

            # Проверяем, что булка найдена и ее имя соответствует ожидаемому
        assert found_bun is not None, f"Булка с именем '{bun_name}' не найдена в базе данных."
        assert found_bun.get_name() == bun_name

    @pytest.mark.parametrize(
        "bun_name, bun_price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ],
    )
    def test_get_price_parametrize(self, database, bun_name, bun_price):
        """
        Проверяет правильность работы метода get_price().
        """
        buns = database.available_buns()
        found_bun = None
        for bun in buns:
            if bun.name == bun_name:
                found_bun = bun
                break

            # Проверяем, что булка найдена и ее имя соответствует ожидаемому
        assert found_bun is not None, f"Булка с именем '{bun_name}' не найдена в базе данных."
        assert found_bun.get_price() == bun_price