import pytest
from unittest.mock import Mock
from data import TestData
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient

# 1. Фикстура для валидных булок
@pytest.fixture(params=TestData.valid_buns)
def valid_bun(request):
    name, price = request.param
    return Bun(name, price)

# 2. Фикстура для невалидных булок
@pytest.fixture(params=TestData.invalid_buns)
def invalid_bun(request):
    name, price = request.param
    with pytest.raises(ValueError):
        Bun(name, price)
    return request.param  # Возвращаем исходные данные для проверки в тестах

# 3. Фикстура для Burger с обработкой ошибок
@pytest.fixture(params=TestData.burger_cases)
def burger_data(request):
    bun_data, ingredients_data, expected_price = request.param
    try:
        bun = Bun(*bun_data) if bun_data else None
        ingredients = [Ingredient(*ingredient) for ingredient in ingredients_data]
        return bun, ingredients, expected_price
    except (ValueError, TypeError):
        pytest.skip("Невалидные данные для создания бургера")

# 4. Мокированные объекты
@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "black bun"
    mock.get_price.return_value = 100
    return mock

@pytest.fixture
def mock_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_type.return_value = "FILLING"
    mock.get_name.return_value = "cutlet"
    mock.get_price.return_value = 50
    return mock

# 5. Фикстура для мокированной базы данных
@pytest.fixture
def mock_database(mocker):
    mock = mocker.Mock(spec=Database)
    mock.available_buns.return_value = [Mock(spec=Bun), Mock(spec=Bun)]
    mock.available_ingredients.return_value = [Mock(spec=Ingredient) for _ in range(6)]
    return mock

# 6. Фикстуры для параметризованных данных
@pytest.fixture(params=TestData.valid_ingredients)
def valid_ingredient(request):
    return Ingredient(*request.param)

@pytest.fixture(params=TestData.invalid_ingredients)
def invalid_ingredient(request):
    with pytest.raises(ValueError):
        Ingredient(*request.param)
    return request.param

@pytest.fixture
def database():
    """Фикстура для тестирования класса Database"""
    return Database()

