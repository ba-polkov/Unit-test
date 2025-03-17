from praktikum.ingredient import Ingredient
from data import IngredientData
import pytest


class TestIngredient:

    def test_get_price(self):
        ingredient = Ingredient(IngredientData.ing_type, IngredientData.ing_name, IngredientData.ing_price)
        assert ingredient.get_price() == IngredientData.ing_price

    def test_get_name(self):
        ingredient = Ingredient(IngredientData.ing_type, IngredientData.ing_name, IngredientData.ing_price)
        assert ingredient.get_name() == IngredientData.ing_name

    def test_get_type(self):
        ingredient = Ingredient(IngredientData.ing_type, IngredientData.ing_name, IngredientData.ing_price)
        assert ingredient.get_type() == IngredientData.ing_type

    @pytest.mark.skip(reason="Валидация данных в классе не реализована.")
    @pytest.mark.parametrize('ing_type, ing_name, ing_price', [[123, 'Неизвестная жидкость', 100.33], ['SAUCE', 123, 100.33], ['SAUCE', 'Неизвестная жидкость', '100.33']])
    def test_invalid_params_type_shows_type_error(self, ing_type, ing_name, ing_price):
        with pytest.raises(TypeError):
            Ingredient(ing_type, ing_name, ing_price)

    @pytest.mark.skip(reason="Валидация данных в классе не реализована.")
    @pytest.mark.parametrize('ing_type, ing_name, ing_price', [['', 'Неизвестная жидкость', 100.33],
                        ['SAUCE', '', 100.33], ['SAUCE', 'Неизвестная жидкость', 0], ['SAUCE', 'Неизвестная жидкость', -100.33]])
    def test_incorrect_params_shows_value_error(self, ing_type, ing_name, ing_price):
        with pytest.raises(ValueError):
            Ingredient(ing_type, ing_name, ing_price)
