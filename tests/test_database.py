import pytest

from praktikum.database import Database
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestDataBase:
    """
    Класс для тестирования функциональности базы данных.

    Содержит тесты для проверки доступности булочек и ингредиентов.
    """

    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ],
        ids=["black_bun", "white_bun", "red_bun"]
    )
    def test_available_buns(
        self,
        index: int,
        expected_name: str,
        expected_price: int
    ) -> None:
        """
        Тест проверки доступности булочек в базе данных.

        :param index: Индекс булочки в списке
        :param expected_name: Ожидаемое название булочки
        :param expected_price: Ожидаемая цена булочки
        """
        # Создаем экземпляр базы данных
        db = Database()
        buns = db.available_buns()

        # Проверяем количество булочек и их характеристики
        assert len(buns) == 3, "Неверное количество булочек"
        assert buns[index].get_name() == expected_name, (
            f"Неверное название булочки: {expected_name}"
        )
        assert buns[index].get_price() == expected_price, (
            f"Неверная цена булочки: {expected_price}"
        )
        assert isinstance(buns[index].get_price(), int), (
            "Цена должна быть целым числом"
        )

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ],
        ids=[
            "hot_sauce",
            "sour_cream",
            "chili_sauce",
            "cutlet",
            "dinosaur",
            "sausage"
        ]
    )
    def test_available_ingredients(
        self,
        index: int,
        expected_type: str,
        expected_name: str,
        expected_price: int
    ) -> None:
        """
        Тест проверки доступности ингредиентов в базе данных.

        :param index: Индекс ингредиента в списке
        :param expected_type: Ожидаемый тип ингредиента
        :param expected_name: Ожидаемое название ингредиента
        :param expected_price: Ожидаемая цена ингредиента
        """
        # Создаем экземпляр базы данных
        db = Database()
        ingredients = db.available_ingredients()

        # Проверяем количество ингредиентов и их характеристики
        assert len(ingredients) == 6, "Неверное количество ингредиентов"
        ingredient = ingredients[index]

        # Проверяем тип ингредиента
        assert ingredient.get_type() == expected_type, (
            f"Неверный тип ингредиента: {expected_type}"
        )

        # Проверяем название и цену
        assert ingredient.get_name() == expected_name, (
            f"Неверное название ингредиента: {expected_name}"
        )
        assert ingredient.get_price() == expected_price, (
            f"Неверная цена ингредиента: {expected_price}"
        )
        assert isinstance(ingredient.get_price(), int), (
            "Цена должна быть целым числом"
        )
        assert isinstance(ingredient.get_name(), str), (
            "Название должно быть строкой"
        )
