import pytest
from praktikum.bun import Bun

# Булочки для тестов
bun_cases = [
    ("black bun", 100.0),
    ("white bun", 200.0),
    ("red bun", 300.0)
]

@pytest.mark.parametrize("bun_name, bun_price", bun_cases)
def test_bun_name_returns_expected(bun_name, bun_price):
    # Проверяем, что имя булки возвращается правильно
    bun = Bun(bun_name, bun_price)
    assert bun.get_name() == bun_name

@pytest.mark.parametrize("bun_name, bun_price", bun_cases)
def test_bun_price_returns_expected(bun_name, bun_price):
    # Убедимся, что стоимость булки совпадает с заданной
    bun = Bun(bun_name, bun_price)
    assert bun.get_price() == bun_price

@pytest.mark.parametrize("bun_name, bun_price", bun_cases)
def test_bun_fields_match_constructor_values(bun_name, bun_price):
    # Поля экземпляра соответствуют значениям, переданным при создании
    bun = Bun(bun_name, bun_price)
    assert bun.name == bun_name
    assert bun.price == bun_price
