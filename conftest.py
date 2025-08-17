import pytest
from unittest.mock import Mock
from praktikum.database import Database

@pytest.fixture
def bun_data():
    return {
        'name': 'black bun',
        'price': 100
    }

@pytest.fixture
def ingredient_data():
    return {
        'sauce': {
            'type': 'SAUCE',
            'name': 'hot sauce',
            'price': 100
        },
        'filling': {
            'type': 'FILLING',
            'name': 'cutlet',
            'price': 100
        }
    }

@pytest.fixture
def mock_bun(bun_data):
    mock = Mock()
    mock.get_name.return_value = bun_data['name']
    mock.get_price.return_value = bun_data['price']
    return mock

@pytest.fixture
def mock_sauce(ingredient_data):
    mock = Mock()
    mock.get_type.return_value = ingredient_data['sauce']['type']
    mock.get_name.return_value = ingredient_data['sauce']['name']
    mock.get_price.return_value = ingredient_data['sauce']['price']
    return mock

@pytest.fixture
def mock_filling(ingredient_data):
    mock = Mock()
    mock.get_type.return_value = ingredient_data['filling']['type']
    mock.get_name.return_value = ingredient_data['filling']['name']
    mock.get_price.return_value = ingredient_data['filling']['price']
    return mock

@pytest.fixture
def db():
    return Database()