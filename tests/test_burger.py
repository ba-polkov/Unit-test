from unittest.mock import Mock
import pytest
from data import Ingredients, Buns
from yandex.burger import Burger
from yandex.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    @pytest.mark.parametrize('ingredient',
                             [
                                 Ingredients.ingredient_name_1,
                                 Ingredients.ingredient_name_2,
                                 Ingredients.ingredient_name_3,
                                 Ingredients.ingredient_name_4
                             ]
                             )
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.ingredients.append(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self):
        burger = Burger()
        burger.ingredients.append(Ingredients.ingredient_name_1)
        burger.ingredients.append(Ingredients.ingredient_name_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self):
        burger = Burger()
        burger.ingredients.append(Ingredients.ingredient_name_1)
        burger.ingredients.append(Ingredients.ingredient_name_2)
        burger.ingredients.append(Ingredients.ingredient_name_3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == Ingredients.ingredient_name_3

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = Buns.bun_price_1
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = Ingredients.ingredient_price_1
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert burger.get_price() == 2066

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = Buns.bun_name_1
        mock_bun.get_price.return_value = Buns.bun_price_1
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = Ingredients.ingredient_name_1
        mock_ingredient.get_price.return_value = Ingredients.ingredient_price_1
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        expected_receipt = f'(==== {Buns.bun_name_1} ====)\n' \
                           f'= sauce {Ingredients.ingredient_name_1} =\n' \
                           f'(==== {Buns.bun_name_1} ====)\n' \
                           f'\nPrice: {Buns.bun_price_1 * 2 + Ingredients.ingredient_price_1}'
        assert burger.get_receipt() == expected_receipt