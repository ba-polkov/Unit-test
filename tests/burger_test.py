import pytest
from unittest.mock import create_autospec
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    return create_autospec(Bun)

@pytest.fixture
def mock_ingredient():
    return create_autospec(Ingredient)

class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients

    def test_move_ingredient(self, burger):
        ingredient1 = create_autospec(Ingredient)
        ingredient2 = create_autospec(Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient1

    @pytest.mark.parametrize('bun_price, ingredient_prices, total_price',
                             [(0.0, [], 0.0),
                              (1255.0, [3000.0], 5510.0),
                              (1255.0, [3000.0, 15.0], 5525.0),
                              (1255.0, [3000.0, 15.0, 424.0], 5949.0)])
    def test_get_price(self, burger, mock_bun, bun_price, ingredient_prices, total_price):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            mock_ingredients = create_autospec(Ingredient)
            mock_ingredients.get_price.return_value = price
            burger.add_ingredient(mock_ingredients)

        expected_price = total_price
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, mock_bun):
        mock_bun.get_name.return_value = 'Краторная булка'
        mock_bun.get_price.return_value = 1255.0
        burger.set_buns(mock_bun)
        ingredient1 = create_autospec(Ingredient)
        ingredient1.get_price.return_value = 3000.0
        ingredient1.get_name.return_value = 'Говяжий метеорит(отбивная)'
        ingredient1.get_type.return_value = 'FILLING'
        ingredient2 = create_autospec(Ingredient)
        ingredient2.get_price.return_value = 15.0
        ingredient2.get_name.return_value = 'Соус традиционный галактический'
        ingredient2.get_type.return_value = 'SAUCE'
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        expected_receipt = '(==== Краторная булка ====)\n= filling Говяжий метеорит(отбивная) =\n= sauce Соус традиционный галактический =\n(==== Краторная булка ====)\n\nPrice: 5525.0'
        assert burger.get_receipt() == expected_receipt
