import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from praktikum.database import Database  # noqa: E402
from praktikum.bun import Bun  # noqa: E402
from praktikum.ingredient import Ingredient  # noqa: E402
from praktikum.ingredient_types import (  # noqa: E402
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestDatabase:
    """Тесты для класса Database с мокированием внешних зависимостей."""

    def test_database_initialization(self, database):
        """Тест инициализации базы данных с предустановленными данными."""
        # Проверяем, что списки инициализированы
        assert isinstance(database.buns, list)
        assert isinstance(database.ingredients, list)

        # Проверяем, что добавлены стандартные булки
        assert len(database.buns) == 3
        assert all(isinstance(bun, Bun) for bun in database.buns)

        # Проверяем, что добавлены стандартные ингредиенты
        assert len(database.ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in database.ingredients)

    def test_available_buns(self, database):
        """Тест получения списка доступных булок."""
        buns = database.available_buns()

        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)

        # Проверяем конкретные булки
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_available_ingredients(self, database):
        """Тест получения списка доступных ингредиентов."""
        ingredients = database.available_ingredients()

        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

        # Проверяем типы ингредиентов
        sauce_count = sum(1 for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE)
        filling_count = sum(1 for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING)

        assert sauce_count == 3
        assert filling_count == 3

    def test_bun_data_integrity(self, database):
        """Тест целостности данных булок."""
        buns = database.available_buns()

        # Проверяем конкретные данные булок
        black_bun = next(bun for bun in buns if bun.get_name() == "black bun")
        assert black_bun.get_price() == 100

        white_bun = next(bun for bun in buns if bun.get_name() == "white bun")
        assert white_bun.get_price() == 200

        red_bun = next(bun for bun in buns if bun.get_name() == "red bun")
        assert red_bun.get_price() == 300

    def test_ingredient_data_integrity(self, database):
        """Тест целостности данных ингредиентов."""
        ingredients = database.available_ingredients()

        # Проверяем соусы
        hot_sauce = next(ing for ing in ingredients if ing.get_name() == "hot sauce")
        assert hot_sauce.get_type() == INGREDIENT_TYPE_SAUCE
        assert hot_sauce.get_price() == 100

        sour_cream = next(ing for ing in ingredients if ing.get_name() == "sour cream")
        assert sour_cream.get_type() == INGREDIENT_TYPE_SAUCE
        assert sour_cream.get_price() == 200

        # Проверяем начинки
        cutlet = next(ing for ing in ingredients if ing.get_name() == "cutlet")
        assert cutlet.get_type() == INGREDIENT_TYPE_FILLING
        assert cutlet.get_price() == 100

        dinosaur = next(ing for ing in ingredients if ing.get_name() == "dinosaur")
        assert dinosaur.get_type() == INGREDIENT_TYPE_FILLING
        assert dinosaur.get_price() == 200

    def test_database_lists_content(self, database):
        """Тест содержимого возвращаемых списков."""
        buns = database.available_buns()
        ingredients = database.available_ingredients()

        # Проверяем, что списки содержат ожидаемое количество элементов
        assert len(buns) == 3
        assert len(ingredients) == 6

        # Проверяем, что возвращенные списки - это те же объекты что и в базе данных
        # (текущее поведение возвращает прямые ссылки)
        assert database.buns is buns
        assert database.ingredients is ingredients

        # Проверяем содержимое списков
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

