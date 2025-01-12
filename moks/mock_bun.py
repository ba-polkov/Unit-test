from unittest.mock import Mock

def set_mock_bun(name, price):
    mock_bun = Mock()
    mock_bun.get_name.return_value = name
    mock_bun.get_price.return_value = price
    return mock_bun