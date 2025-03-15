from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    ing_type = 'SAUCE'
    ing_name = 'Неизвестная жидкость'
    ing_price = 100.33

    def test_get_price(self):
        ingredient = Ingredient(self.ing_type, self.ing_name, self.ing_price)
        assert ingredient.get_price() == self.ing_price

    def test_get_name(self):
        ingredient = Ingredient(self.ing_type, self.ing_name, self.ing_price)
        assert ingredient.get_name() == self.ing_name

    def test_get_type(self):
        ingredient = Ingredient(self.ing_type, self.ing_name, self.ing_price)
        assert ingredient.get_type() == self.ing_type

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
