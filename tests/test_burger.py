import pytest
import random
from unittest.mock import Mock
from praktikum.burger import Burger
from helpers import *

INGREDIENT_QUANTITY = (1, 3, 6, 10)


class TestBurger:

    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def mock_bun(self):
        def _set_bun(bun_data):
            bun = Mock()
            bun.get_name.return_value = bun_data[0]
            bun.get_price.return_value = bun_data[1]
            return bun

        return _set_bun

    @pytest.fixture
    def mock_ingredient(self):
        def _set_ingredient(ingredient_data):
            ingredient = Mock()
            ingredient.get_type.return_value = ingredient_data[0]
            ingredient.get_name.return_value = ingredient_data[1]
            ingredient.get_price.return_value = ingredient_data[2]
            return ingredient

        return _set_ingredient

    @pytest.fixture
    def setup_ingredients(self, burger, mock_ingredient):
        def _add_ingredient(ingredient_quantity):
            ingredient_mock_list = []
            for _ in range(ingredient_quantity):
                ingredient_data = generate_ingredient_data()
                print(f'Ingredient: type={ingredient_data[0]}, name={ingredient_data[1]}, price={ingredient_data[2]}')

                ingredient_mock = mock_ingredient(ingredient_data)
                ingredient_mock_list.append(ingredient_mock)
                burger.add_ingredient(ingredient_mock)
            return ingredient_mock_list

        return _add_ingredient

    @pytest.mark.repeat(2)
    def test_set_buns(self, burger, mock_bun):
        bun_data = generate_bun_data()
        print(f'Bun: name={bun_data[0]}, price={bun_data[1]}')

        bun = mock_bun(bun_data)
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_add_one(self, burger, mock_ingredient):
        ingredient_data = generate_ingredient_data()
        print(f'Ingredient: type={ingredient_data[0]}, name={ingredient_data[1]}, price={ingredient_data[2]}')

        ingredient = mock_ingredient(ingredient_data)
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize("ingredient_quantity", (0, 3, 6, 10))
    def test_add_ingredient_add_several(self, burger, setup_ingredients, ingredient_quantity):
        ingredient_mock_list = setup_ingredients(ingredient_quantity)

        assert len(burger.ingredients) == ingredient_quantity
        assert burger.ingredients == ingredient_mock_list

    @pytest.mark.parametrize("ingredient_quantity", (1, 3, 6, 10))
    def test_remove_ingredient_existing_ingredients(self, burger, setup_ingredients, ingredient_quantity):
        ingredient_mock_list = setup_ingredients(ingredient_quantity)

        # выбираем индекс ингредиента
        index = random.randint(0, ingredient_quantity - 1)
        print(index)

        # удаляем ингредиент
        burger.remove_ingredient(index)

        assert len(burger.ingredients) == ingredient_quantity - 1
        assert ingredient_mock_list[index] not in burger.ingredients

    @pytest.mark.parametrize("ingredient_quantity", (2, 3, 6, 10))
    def test_move_ingredient(self, burger, setup_ingredients, ingredient_quantity):
        ingredient_mock_list = setup_ingredients(ingredient_quantity)

        # выбираем индекс ингредиента
        old_index, new_index = random.sample(range(0, ingredient_quantity), 2)
        print(old_index, new_index)

        # перемещаем ингредиент
        burger.move_ingredient(old_index, new_index)

        assert len(burger.ingredients) == ingredient_quantity
        assert burger.ingredients[new_index] == ingredient_mock_list[old_index]

    def test_get_price(self, burger, mock_bun, mock_ingredient):
        bun, ingredient = mock_bun(generate_bun_data()), mock_ingredient(generate_ingredient_data())

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert burger.get_price() == 2 * bun.get_price() + ingredient.get_price()

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        bun, ingredient = mock_bun(generate_bun_data()), mock_ingredient(generate_ingredient_data())

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'(==== {bun.get_name()} ====)\n= {ingredient.get_type().lower()} {ingredient.get_name()} =\n(==== {bun.get_name()} ====)\n\nPrice: {burger.get_price()}'

        assert burger.get_receipt() == expected_receipt
