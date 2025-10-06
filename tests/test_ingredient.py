from unittest.mock import Mock

import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type",
        [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING],
        ids=["SAUCE", "FILLING"],
    )
    def test_get_type__with_valid_constant__returns_same(self, ingredient_type):
        type_provider = Mock(return_value=ingredient_type)
        ingredient = Ingredient(type_provider(), "Кетчунез", 1.0)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        "name",
        ["Сыр", "BBQ", "Салат-микс", "Соус №1", "  spaced  ", "Bún", "x" * 10],
        ids=["ru", "en", "hyphen", "№", "spaces", "diacritics", "long"],
    )
    def test_get_name_returns_constructor_value(self, name):
        type_provider = Mock(return_value=INGREDIENT_TYPE_SAUCE)
        ingredient = Ingredient(type_provider(), name, 1.0)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [0, 1, 1.0, 2.5, 3.75, 1000000],
        ids=["zero", "int", "float1_0", "float2_5", "float3_75", "big"],
    )
    def test_get_price_returns_constructor_value(self, price):
        type_provider = Mock(return_value=INGREDIENT_TYPE_FILLING)
        ingredient = Ingredient(type_provider(), "BBQ", price)
        assert ingredient.get_price() == price

