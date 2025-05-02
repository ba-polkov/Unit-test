#Названия и цены булочек
BUN_NAME_1 = "bun_1"
BUN_NAME_2 = "bun_2"
BUN_PRICE = 100

#Названия и цены ингридиентов
SAUCE_NAME = "sauce_1"
FILLING_NAME = "filling_1"
SAUCE_PRICE = 135
FILLING_PRICE = 120


def create_mock_ingredient(name, price):
    from unittest.mock import Mock
    from Diplom_1.practicum.ingredient import Ingredient
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock