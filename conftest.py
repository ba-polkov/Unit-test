import pytest

from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Краторная булка N-200i"
    bun.get_price.return_value = 1255.0
    return bun

@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "Соус Spicy-X"
    sauce.get_price.return_value = 90.0
    return sauce

@pytest.fixture
def mock_main():
    main = Mock()
    main.get_type.return_value = "MAIN"
    main.get_name.return_value = "Филе Люминесцентного тетраодонтимформа"
    main.get_price.return_value = 988.0
    return main


