from unittest.mock import Mock



def set_mock_ingredient(name, price, type_ingredient):
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_price.return_value = price
    mock_ingredient.get_type.return_value = type_ingredient
    return mock_ingredient
