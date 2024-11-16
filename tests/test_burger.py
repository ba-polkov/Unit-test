import unittest
from ..praktikum.burger import Burger
from ..praktikum.bun import Bun
from ..praktikum.ingredient import Ingredient

@pytest.fixture
def mock_bun(mocker):
    bun = mocker.Mock(spec=Bun)
    bun.get_price.return_value = 100
    bun.get_name.return_value = "black bun"
    return bun

@pytest.fixture
def mock_ingredient_filling(mocker):
    ingredient = mocker.Mock(spec=Ingredient)
    ingredient.get_price.return_value = 100
    ingredient.get_name.return_value = "black bun"
    ingredient.get_type.return_value = "cutlet"
    return ingredient

@pytest.fixture
def mock_ingredient_sauce(mocker):
    ingredient = mocker.Mock(spec=Ingredient)
    ingredient.get_price.return_value = 100
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_type.return_value = "sauce"
    return ingredient

class TestBurger(unittest.TestCase):
    def setUp(self):
        self.burger = Burger()
        self.bun = Bun(name="black bun", price=100)
        self.ingredient1 = Ingredient(ingredient_type="filling", name="cutlet", price=100)
        self.ingredient2 = Ingredient(ingredient_type="sauce", name="hot sauce", price=100)

    def test_set_buns(self):
        self.burger.set_buns(self.bun)
        self.assertEqual(self.burger.bun, self.bun)

    def test_add_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        self.assertIn(self.ingredient1, self.burger.ingredients)

    def test_remove_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        self.burger.remove_ingredient(0)
        self.assertNotIn(self.ingredient1, self.burger.ingredients)

    def test_move_ingredient(self):
        self.burger.add_ingredient(self.ingredient1)
        self.burger.add_ingredient(self.ingredient2)
        self.burger.move_ingredient(0, 1)
        self.assertEqual(self.burger.ingredients[1], self.ingredient1)

    def test_burger_price(mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)

        expected_price = mock_bun.get_price() * 2 + mock_ingredient_filling.get_price() + mock_ingredient_sauce.get_price()
        assert burger.get_price() == expected_price

    def test_burger_receipt(mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)

        expected_receipt = (
            f'(==== {mock_bun.get_name()} ====)\n'
            f'= {mock_ingredient_filling.get_type().lower()} {mock_ingredient_filling.get_name()} =\n'
            f'= {mock_ingredient_sauce.get_type().lower()} {mock_ingredient_sauce.get_name()} =\n'
            f'(==== {mock_bun.get_name()} ====)\n'
            f'Price: {burger.get_price()}'
        )

        assert burger.get_receipt() == expected_receipt


if __name__ == '__main__':
    unittest.main()