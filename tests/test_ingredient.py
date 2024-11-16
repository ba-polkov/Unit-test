import unittest
from ..ingredient import Ingredient

@pytest.mark.parametrize("ingredient_type, name, price, expected_type, expected_name, expected_price", [
    ("filling", "cutlet", 1.0, "filling", "dinosaur", 100),
    ("sauce", "hot sauce", 0.5, "sauce", "sour cream", 100)
])
def test_ingredient(ingredient_type, name, price, expected_type, expected_name, expected_price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == expected_type
    assert ingredient.get_name() == expected_name
    assert ingredient.get_price() == expected_price

class TestIngredient(unittest.TestCase):
    def setUp(self):
        self.ingredient_filling = Ingredient(ingredient_type="filling", name="cutlet", price=100)
        self.ingredient_sauce = Ingredient(ingredient_type="sauce", name="hot sauce", price=100)

    def test_get_price(self):
        self.assertEqual(self.ingredient_filling.get_price(), 100)
        self.assertEqual(self.ingredient_sauce.get_price(), 100)

    def test_get_name(self):
        self.assertEqual(self.ingredient_filling.get_name(), "cutlet")
        self.assertEqual(self.ingredient_sauce.get_name(), "hot sauce")

    def test_get_type(self):
        self.assertEqual(self.ingredient_filling.get_type(), "filling")
        self.assertEqual(self.ingredient_sauce.get_type(), "sauce")


if __name__ == '__main__':
    unittest.main()