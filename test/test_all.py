from praktikum.burger import *
from conftest import *
from praktikum.database import Database


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price


class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == mock_ingredient

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert "black bun" in receipt
        assert "cutlet" in receipt
        assert "Price: 250" in receipt


class TestIngredient:
    def test_get_name(self):
        ingredient = Ingredient("FILLING", "cutlet", 100)
        assert ingredient.get_name() == "cutlet"

    def test_get_price(self):
        ingredient = Ingredient("SAUCE", "sour cream", 200)
        assert ingredient.get_price() == 200

    def test_get_type(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 150)
        assert ingredient.get_type() == "SAUCE"

class TestDatabase:
    def setup_method(self):
        self.database = Database()

    def test_available_buns(self):
        buns = self.database.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)
        assert len(buns) == 3

    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        assert len(ingredients) == 6