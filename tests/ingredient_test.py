from src.ingredient import Ingredient


class TestIngredient:
    def test_ingredient_init(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        assert ingredient.name == "hot sauce"
        assert ingredient.type == "SAUCE"
        assert ingredient.price == 100

    def test_get_price_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        assert ingredient.get_price() == 100

    def test_get_name_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"

    def test_get_type_ingredient(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100)
        assert ingredient.get_type() == "SAUCE"
