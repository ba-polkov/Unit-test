import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def sample_bun():
    """Фикстура для создания тестовой булки."""
    return Bun("test bun", 100.0)


@pytest.fixture
def sample_ingredient():
    """Фикстура для создания тестового ингредиента."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50.0)


@pytest.fixture
def mock_bun():
    """Фикстура для мок-объекта булки."""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "mocked bun"
    mock.get_price.return_value = 150.0
    return mock


@pytest.fixture
def mock_ingredient():
    """Фикстура для мок-объекта ингредиента."""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "mocked ingredient"
    mock.get_price.return_value = 75.0
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock


@pytest.fixture
def database():
    """Фикстура для создания базы данных с тестовыми данными."""
    return Database()


@pytest.fixture
def empty_burger():
    """Фикстура для создания пустого бургера."""
    return Burger()


@pytest.fixture
def burger_with_bun(mock_bun):
    """Фикстура для создания бургера с булкой."""
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger


@pytest.fixture
def burger_with_ingredients(mock_bun, mock_ingredient):
    """Фикстура для создания бургера с булкой и ингредиентами."""
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger