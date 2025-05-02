from praktikum import ingredient_types


class TestIngredient:

    def test_get_price(self, ingredient):

        assert ingredient.get_price() == 60

    def test_get_name(self, ingredient):

        assert ingredient.get_name() == 'Соус'

    def test_get_type(self, ingredient):

        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_SAUCE
