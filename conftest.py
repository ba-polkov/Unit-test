import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def make_mock_bun(name="тестовая булка", price=50.5):
    mock_bun = MagicMock(spec=Bun)
    mock_bun.get_name.return_value = name
    mock_bun.get_price.return_value = price
    return mock_bun

def make_mock_ingredient(type_="начинка", name="тестовый ингредиент", price=33.3):
    mock_ing = MagicMock(spec=Ingredient)
    mock_ing.get_type.return_value = type_
    mock_ing.get_name.return_value = name
    mock_ing.get_price.return_value = price
    return mock_ing