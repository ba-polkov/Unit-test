import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock



@pytest.fixture
def mock_bun():
    """Фикстура для мока булочки"""
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce():
    """Фикстура для мока соуса"""
    sauce = Mock(spec=Ingredient)
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 50.0
    return sauce


@pytest.fixture
def mock_filling():
    """Фикстура для мока начинки"""
    filling = Mock(spec=Ingredient)
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 75.0
    return filling


@pytest.fixture
def prepared_burger(mock_bun, mock_sauce, mock_filling):
    """Фикстура для готового бургера с ингредиентами"""
    from praktikum.burger import Burger
    burger = Burger()  # Создаем бургер непосредственно в фикстуре
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    return burger

