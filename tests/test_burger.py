from helpers.helper import get_receipt


class TestBurger:

    def test_set_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient_sauce, mock_ingredient_filling):
        ingredients = [mock_ingredient_sauce, mock_ingredient_filling]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        assert burger.ingredients == ingredients

    def test_remove_ingredients(self, burger_with_ingredients):
        while burger_with_ingredients.ingredients:
            burger_with_ingredients.remove_ingredient(0)
        assert not burger_with_ingredients.ingredients

    def test_move_ingredient(self, burger_with_ingredients):
        ingredients_before = [i.name for i in burger_with_ingredients.ingredients]
        burger_with_ingredients.move_ingredient(0, 1)
        ingredients_after = [i.name for i in burger_with_ingredients.ingredients]
        assert ingredients_before != ingredients_after

    def test_burger_price(self, burger_with_price):
        mock_burger, expected_price = burger_with_price
        assert mock_burger.get_price() == expected_price

    def test_burger_receipt(self, burger_with_price):
        mock_burger, price = burger_with_price
        assert mock_burger.get_receipt() == get_receipt(mock_burger)
