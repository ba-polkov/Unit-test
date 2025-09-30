import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest  # noqa: E402
from praktikum.ingredient import Ingredient  # noqa: E402
from praktikum.ingredient_types import (  # noqa: E402
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestIngredient:
    """Тесты для класса Ingredient с параметризацией различных типов ингредиентов."""

    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0,
             INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0,
             INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100.0,
             INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0,
             INGREDIENT_TYPE_FILLING, "dinosaur", 200.0),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300.0,
             INGREDIENT_TYPE_SAUCE, "chili sauce", 300.0),
            (INGREDIENT_TYPE_FILLING, "sausage", 300.0,
             INGREDIENT_TYPE_FILLING, "sausage", 300.0),
        ]
    )
    def test_ingredient_initialization(
        self, ingredient_type, name, price,
        expected_type, expected_name, expected_price
    ):
        """Тест инициализации ингредиента с различными параметрами."""
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 50.0),
        (INGREDIENT_TYPE_SAUCE, "mayonnaise", 75.0),
        (INGREDIENT_TYPE_FILLING, "cheese", 120.0),
        (INGREDIENT_TYPE_FILLING, "lettuce", 30.0),
        ("", "unknown", 0.0),  # Пустой тип
        (INGREDIENT_TYPE_SAUCE, "", 100.0),  # Пустое название
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price):
        """Тест получения типа ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "mustard", 60.0),
        (INGREDIENT_TYPE_SAUCE, "bbq sauce", 90.0),
        (INGREDIENT_TYPE_FILLING, "tomato", 40.0),
        (INGREDIENT_TYPE_FILLING, "onion", 25.0),
        (INGREDIENT_TYPE_SAUCE, "special sauce", 200.0),
    ])
    def test_ingredient_get_name(self, ingredient_type, name, price):
        """Тест получения названия ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "garlic sauce", 80.0),
        (INGREDIENT_TYPE_FILLING, "bacon", 150.0),
        (INGREDIENT_TYPE_SAUCE, "free sauce", 0.0),  # Бесплатный соус
        (INGREDIENT_TYPE_FILLING, "premium beef", 500.0),  # Дорогая начинка
        (INGREDIENT_TYPE_SAUCE, "negative price", -10.0),  # Отрицательная цена
    ])
    def test_ingredient_get_price(self, ingredient_type, name, price):
        """Тест получения цены ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    def test_ingredient_attributes_access(self, sample_ingredient):
        """Тест доступа к атрибутам ингредиента через геттеры."""
        ingredient = sample_ingredient

        # Проверяем, что геттеры возвращают правильные значения
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredient.get_name() == "test sauce"
        assert ingredient.get_price() == 50.0

        # Проверяем, что прямое изменение атрибутов влияет на геттеры
        ingredient.type = INGREDIENT_TYPE_FILLING
        ingredient.name = "modified sauce"
        ingredient.price = 999.0

        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
        assert ingredient.get_name() == "modified sauce"
        assert ingredient.get_price() == 999.0
