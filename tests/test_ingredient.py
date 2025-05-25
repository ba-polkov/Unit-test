import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    # Проверка создания ингредиента и работы методов get_type, get_name, get_price
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),  # Соус с обычной ценой
            (INGREDIENT_TYPE_FILLING, "cutlet", 200.0),  # Начинка с обычной ценой
            (INGREDIENT_TYPE_SAUCE, "free sauce", 0.0),  # Соус с нулевой ценой
            (INGREDIENT_TYPE_FILLING, "VEGGIE PATTY", 150.50),  # Начинка с именем в верхнем регистре
        ],
    )
    def test_ingredient_creation_and_getters(self, ingredient_type, name, price):
        # Создаем ингредиент с заданными параметрами
        ingredient = Ingredient(ingredient_type, name, price)

        # Проверяем, что тип ингредиента соответствует заданному
        assert ingredient.get_type() == ingredient_type, f"Expected type {ingredient_type}, got {ingredient.get_type()}"

        # Проверяем, что имя ингредиента соответствует заданному
        assert ingredient.get_name() == name, f"Expected name {name}, got {ingredient.get_name()}"

        # Проверяем, что цена ингредиента соответствует заданной
        assert ingredient.get_price() == price, f"Expected price {price}, got {ingredient.get_price()}"