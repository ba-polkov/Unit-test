from unittest.mock import Mock

# Мок булочки
mock_bun = Mock()
mock_bun.get_name.return_value = "Новая булка V-100500"
mock_bun.get_price.return_value = 1100.0

# Моки ингредиентов
mock_ingredient1 = Mock()
mock_ingredient1.get_name.return_value = "Morti котлетка"
mock_ingredient1.get_type.return_value = "main"
mock_ingredient1.get_price.return_value = 50.0

mock_ingredient2 = Mock()
mock_ingredient2.get_name.return_value = "Соус Rick"
mock_ingredient2.get_type.return_value = "sauce"
mock_ingredient2.get_price.return_value = 1000.0