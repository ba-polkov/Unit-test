import pytest
from unittest.mock import Mock, patch
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    """Тест-кейсы для класса Database"""
    
    @pytest.fixture
    def database(self):
        """Фикстура для создания экземпляра Database"""
        return Database()
    
    @pytest.fixture
    def mock_bun(self):
        """Фикстура для создания mock-булочки"""
        bun = Mock(spec=Bun)
        bun.get_name.return_value = "Краторная булка"
        return bun
    
    @pytest.fixture
    def mock_ingredient(self):
        """Фикстура для создания mock-ингредиента"""
        ingredient = Mock(spec=Ingredient)
        ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient.get_name.return_value = "Сырный соус"
        return ingredient

    # Тест-кейс 1: Проверка получения доступных булочек
    def test_available_buns(self, database, mock_bun):
        """Проверка метода available_buns()"""
        # Подменяем список булочек в базе данных
        database.buns = [mock_bun]
        
        buns = database.available_buns()
        assert len(buns) == 1
        assert buns[0].get_name() == "Краторная булка"

    # Тест-кейс 2: Проверка получения доступных ингредиентов
    def test_available_ingredients(self, database, mock_ingredient):
        """Проверка метода available_ingredients()"""
        # Подменяем список ингредиентов в базе данных
        database.ingredients = [mock_ingredient]
        
        ingredients = database.available_ingredients()
        assert len(ingredients) == 1
        assert ingredients[0].get_name() == "Сырный соус"
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE

    # Тест-кейс 3: Проверка инициализации данных
    @patch('praktikum.database.Database.load_initial_data')
    def test_init_calls_load_data(self, mock_load, database):
        """Проверка вызова load_initial_data при инициализации"""
        Database()
        mock_load.assert_called_once()

    # Тест-кейс 4: Параметризованный тест для разных типов ингредиентов
    @pytest.mark.parametrize('ingredient_type, expected_count', [
        (INGREDIENT_TYPE_SAUCE, 3),  # 3 соуса в начальных данных
        (INGREDIENT_TYPE_FILLING, 3)  # 3 начинки в начальных данных
    ])
    def test_ingredient_types_in_database(self, database, ingredient_type, expected_count):
        """Проверка корректности типов ингредиентов в базе"""
        ingredients = database.available_ingredients()
        count = sum(1 for ing in ingredients if ing.get_type() == ingredient_type)
        assert count == expected_count

    # Тест-кейс 5: Проверка количества булочек в базе
    def test_buns_count_in_database(self, database):
        """Проверка количества булочек в начальных данных"""
        buns = database.available_buns()
        assert len(buns) == 3  # 3 булочки в начальных данных

    # Тест-кейс 6: Проверка работы с пустой базой
    def test_empty_database(self, database):
        """Проверка работы с пустой базой данных"""
        database.buns = []
        database.ingredients = []
        
        assert len(database.available_buns()) == 0
        assert len(database.available_ingredients()) == 0