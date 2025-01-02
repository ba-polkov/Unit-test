from unittest.mock import patch
from praktikum.database import Database


class TestDataBase:
    @patch("praktikum.database.Bun", autospec=True)
    def test_available_buns(self, mockbun):
        mock_bun1 = mockbun.return_value
        mock_bun1.get_name.return_value = "Mock бутофория"
        mock_bun1.get_price.return_value = 100.0
        database = Database()
        database.buns = [mock_bun1]
        buns = database.available_buns()

        assert buns == [mock_bun1], f'Метод available_buns должен возвращать замоканную булочку.'
