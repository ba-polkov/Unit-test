from praktikum.ingredient import Ingredient


class TestIngredient:

    def test_get_price(self):
        types = 'souse'
        name = 'test'
        price = 99.9
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_price() == price

    def test_get_name(self):
        types = 'souse'
        name = 'test'
        price = 99.9
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_name() == name

    def test_get_type(self):
        types = 'souse'
        name = 'test'
        price = 99.9
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_type() == types
