from unittest.mock import Mock


class TestBurger:

    def test_set_buns(self, burger):
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0,1)

        assert burger.ingredients[1] == mock_ingredient_1

    def test_get_price(self, bun, ingredient, burger):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 2200.0

    def test_get_receipt(self, bun, ingredient, burger):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert bun.name and ingredient.name in burger.get_receipt()

