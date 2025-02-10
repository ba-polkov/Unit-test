from praktikum.praktikum import Ingredient


class TestIngredient:

    def test_ingredient_get_name(self):
        ingredient = Ingredient('SAUCE', 'Соус XX', 50)
        assert ingredient.get_name() == 'Соус XX'

    def test_ingredient_get_price(self):
        ingredient = Ingredient('SAUCE', 'Соус XX', 50)
        assert ingredient.get_price() == 50

    def test_ingredient_get_type(self):
        ingredient = Ingredient('SAUCE', 'Соус XX', 50)
        assert ingredient.get_type() == 'SAUCE'
