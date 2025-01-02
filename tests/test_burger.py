import pytest

from praktikum.bun import Bun
from unittest.mock import patch
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns_bun_is_set(self):
        bun = Bun('Гранд', 150.0)
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun == bun, f'Метод set_buns не установил булочку.'

    @pytest.mark.parametrize(
        'ingredient_type, name, price', [
            (INGREDIENT_TYPE_SAUCE, 'Кетчуп', 30.0),
            (INGREDIENT_TYPE_FILLING, 'Катлета', 80.0)
        ]
    )
    @patch('praktikum.ingredient.Ingredient')
    def test_add_ingredient_check_addition_of_ingredients_to_list(self, mockIngredient, ingredient_type, name, price):
        mock_ingredient = mockIngredient.return_value
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient], f'Ингредиенты должены быть добавлены в список.'

    @patch('praktikum.ingredient.Ingredient')
    def test_remove_ingredient_removing_ingredients_from_list(self, mockIngredient):
        mock_ingredient1 = mockIngredient.return_value
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = 'Чили'
        mock_ingredient1.get_price.return_value = 5.0
        mock_ingredient2 = mockIngredient.return_value
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = 'Катлета'
        mock_ingredient2.get_price.return_value = 10.0
        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.remove_ingredient(0)

        assert burger.ingredients == [mock_ingredient2], f'Ингредиенты должны быть удалены по индексу из списка.'

    @patch('praktikum.ingredient.Ingredient')
    def test_move_ingredient_first_to_last(self, mockIngredient):
        mock_ingredient1 = mockIngredient.return_value
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = 'Майонез'
        mock_ingredient1.get_price.return_value = 5.0

        mock_ingredient2 = mockIngredient.return_value
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = 'Катлета'
        mock_ingredient2.get_price.return_value = 100.0

        mock_ingredient3 = mockIngredient.return_value
        mock_ingredient3.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient3.get_name.return_value = 'Чили'
        mock_ingredient3.get_price.return_value = 8.0

        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [mock_ingredient2, mock_ingredient3, mock_ingredient1], \
            f'Первый ингредиент должен быть перемещен в конец.'
