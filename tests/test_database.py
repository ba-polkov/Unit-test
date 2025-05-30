from unittest.mock import patch, MagicMock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


class TestDatabase:

    # Проверка инициализации базы данных
    def test_initialization(self, database):
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6
        assert isinstance(database.buns[0], Bun)
        assert isinstance(database.ingredients[0], Ingredient)

    # Проверка инициализации с моками
    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_initialization_with_mocks(self, mock_ingredient, mock_bun):
        # Создать тестовую базу
        db = Database()

        # Проверяем что методы были вызваны
        assert mock_bun.call_count == 3
        assert mock_ingredient.call_count == 6

    # Проверка списка доступных булок
    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    # Тест проверяет доступные булки с моками
    @patch('praktikum.database.Database')
    def test_available_buns_with_mock(self, mock_db):
        # Настроить мок
        mock_bun = MagicMock()
        mock_db.available_buns.return_value = [mock_bun]

        # Протестировать
        result = mock_db.available_buns()

        # Проверить
        mock_db.available_buns.assert_called_once()
        assert len(result) == 1


    # Проверка списка доступных ингредиентов
    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

        # Проверка соусов
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100

        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200

        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_price() == 300

        # Проверка начинок
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100

        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200

        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_price() == 300
