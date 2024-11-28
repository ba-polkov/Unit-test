import allure
import pytest
from unittest.mock import Mock

from data import BurgerConsist as bc


@allure.title('создаем мок булки - white bun')
@pytest.fixture(scope='function')
def mock_white_bun():
    mock_white_bun = Mock()
    mock_white_bun.name = bc.FIRST_BUN_NAME
    mock_white_bun.price = bc.FIRST_BUN_PRICE
    mock_white_bun.return_value.get_name = bc.FIRST_BUN_NAME
    mock_white_bun.return_value.get_price = bc.FIRST_BUN_PRICE
    return mock_white_bun


@allure.title('создаем мок булки 2 - red bun')
@pytest.fixture(scope='function')
def mock_red_bun():
    mock_red_bun = Mock()
    mock_red_bun.name = bc.SECOND_BUN_NAME
    mock_red_bun.price = bc.SECOND_BUN_PRICE
    mock_red_bun.return_value.get_name = bc.SECOND_BUN_NAME
    mock_red_bun.return_value.get_price = bc.SECOND_BUN_PRICE
    return mock_red_bun


@allure.title('создаем мок соуса')
@pytest.fixture(scope='function')
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.type = bc.INGREDIENT_TYPE_SAUCE
    mock_sauce.name = bc.INGREDIENT_TYPE_SAUCE_NAME
    mock_sauce.price = bc.SAUCE_PRICE
    mock_sauce.return_value.get_type = bc.INGREDIENT_TYPE_SAUCE
    mock_sauce.return_value.get_name = bc.INGREDIENT_TYPE_SAUCE_NAME
    mock_sauce.return_value.get_price = bc.SAUCE_PRICE
    return mock_sauce


@allure.title('создаем мок начинки')
@pytest.fixture(scope='function')
def mock_filling():
    mock_filling = Mock()
    mock_filling.type = bc.INGREDIENT_TYPE_FILLING
    mock_filling.name = bc.INGREDIENT_TYPE_FILLING_NAME
    mock_filling.price = bc.FILLING_PRICE
    mock_filling.return_value.get_type = bc.INGREDIENT_TYPE_FILLING
    mock_filling.return_value.get_name = bc.INGREDIENT_TYPE_FILLING_NAME
    mock_filling.return_value.get_price = bc.FILLING_PRICE
    return mock_filling

