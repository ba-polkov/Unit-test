import pytest

from praktikum.ingredient import Ingredient
from src.data import INGREDIENTS_DATA, INGREDIENTS_WITH_NEGATIVE_PRICES


class TestIngredient:
    # Проверка инициализации ингредиента
    def test_ingredient_init_sets_type_name_and_price_correctly(self):
        ingredient_type, name, price = INGREDIENTS_DATA[0]
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type, \
            f"Ожидался тип ингредиента '{ingredient_type}', получен '{ingredient.type}'"
        assert ingredient.name == name, \
            f"Ожидалось название ингредиента '{name}', получено '{ingredient.name}'"
        assert ingredient.price == price, \
            f"Ожидалась цена ингредиента '{price}', получена '{ingredient.price}'"

    # Проверка геттеров
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS_DATA)
    def test_ingredient_get_type_returns_correct_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type, \
            f"Ожидался тип ингредиента '{ingredient_type}', получен '{ingredient.type}'"

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS_DATA)
    def test_ingredient_get_name_returns_correct_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name, \
            f"Ожидалось название ингредиента '{name}', получено '{ingredient.name}'"

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS_DATA)
    def test_ingredient_get_price_returns_correct_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, \
            f"Ожидалась цена ингредиента '{price}', получена '{ingredient.price}'"

    # Проверка отрицательных цен
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS_WITH_NEGATIVE_PRICES)
    @pytest.mark.xfail(reason = 'Negative price should raise ValueError, but not implemented - this is a bug')
    def test_ingredient_with_negative_price_raises_value_error(self, ingredient_type, name, price):
        with pytest.raises(ValueError, match="Цена булочки не может быть отрицательной"):
            Ingredient(ingredient_type, name, price)