# conftest.py

import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from unittest.mock import Mock


@pytest.fixture
def default_bun():
    """Фикстура для стандартной булки"""
    return Bun("Краторная булка N-200i", 1255)

@pytest.fixture
def empty_burger():
    """Фикстура для пустого бургера"""
    return Burger()

@pytest.fixture
def prepared_burger(default_bun):
    """Фикстура для собранного бургера (булка + 2 ингредиента)"""
    burger = Burger()
    burger.set_buns(default_bun)
    burger.add_ingredient(Ingredient("SAUCE", "Соус фирменный Space Sauce", 80))
    burger.add_ingredient(Ingredient("FILLING", "Биокотлета из марсианской Магнолии", 424))
    return burger

# Параметризованные фикстуры
@pytest.fixture(params=[
    ("Краторная булка N-200i", 1255),
    ("Флюоресцентная булка R2-D3", 988)
], ids=["krator_bun", "fluorescent_bun"])
def parametrized_bun(request):
    return Bun(*request.param)

@pytest.fixture(params=[
    ("SAUCE", "Соус фирменный Space Sauce", 80),
    ("FILLING", "Биокотлета из марсианской Магнолии", 424)
], ids=["sauce", "filling"])
def parametrized_ingredient(request):
    return Ingredient(*request.param)

# Мокированные объекты
@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Мок булки"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_ingredient():
    ingr = Mock(spec=Ingredient)
    ingr.get_type.return_value = "SAUCE"
    ingr.get_name.return_value = "Мок соуса"
    ingr.get_price.return_value = 50
    return ingr

@pytest.fixture
def burger_with_mocks(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger

# Параметризованные фикстуры
@pytest.fixture(params=[80, 100, 150], ids=["cheap", "medium", "expensive"])
def parametrized_ingredient_price(request):
    ingr = Mock(spec=Ingredient)
    ingr.get_price.return_value = request.param
    return ingr