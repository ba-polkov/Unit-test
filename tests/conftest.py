import pytest
from unittest.mock import Mock

from Diplom_1.data import MockBurger
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.burger import Burger
from Diplom_1.praktikum.ingredient import Ingredient


# Фикстура для булочки
@pytest.fixture
def bun_fixture():
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = MockBurger.BUN_NAME
    mock_bun.get_price.return_value = MockBurger.BUN_PRICE
    return mock_bun

# Фикстура для начинок
@pytest.fixture
def filling_fixture():
    mock_filling = Mock(spec=Ingredient)
    mock_filling.get_price.return_value = MockBurger.FILLING_PRICE
    mock_filling.get_name.return_value = MockBurger.FILLING_NAME
    mock_filling.get_type.return_value = MockBurger.FILLING_TYPE
    return mock_filling

# Фикстура для соуса
@pytest.fixture
def sauce_fixture():
    mock_sauce = Mock(spec=Ingredient)
    mock_sauce.get_price.return_value = MockBurger.SAUCE_PRICE
    mock_sauce.get_name.return_value = MockBurger.SAUCE_NAME
    mock_sauce.get_type.return_value = MockBurger.SAUCE_TYPE
    return mock_sauce

    # Фикстура для бургера с булочкой
@pytest.fixture
def burger_fixture(bun_fixture, filling_fixture, sauce_fixture):
    burger = Burger()
    burger.set_buns(bun_fixture)
    burger.add_ingredient(filling_fixture)
    burger.add_ingredient(sauce_fixture)
    return burger
