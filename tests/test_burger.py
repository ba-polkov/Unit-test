import pytest
from unittest.mock import Mock

class TestBurger:
    def test_set_buns(self, make_burger, bun):
        burger = make_burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, make_burger, ingredient):
        burger = make_burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_remove_ingredient(self, make_burger, ingredient):
        burger = make_burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, make_burger):
        burger = make_burger()
        ingredient_1 = Mock()
        ingredient_1.get_name.return_value = "Cheese"
        ingredient_2 = Mock()
        ingredient_2.get_name.return_value = "Ketchup"

        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]

    def test_remove_invalid_index(self, make_burger, ingredient):
        burger = make_burger()
        burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.remove_ingredient(1)

    def test_get_receipt(self, make_burger, bun, ingredient):
        burger = make_burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        expected_receipt = f'(==== {bun.get_name()} ====)\n' \
                           f'= {ingredient.get_type().lower()} {ingredient.get_name()} =\n' \
                           '\n' \
                           f'Price: {burger.get_price()}'

        assert burger.get_receipt() == expected_receipt

    @pytest.mark.parametrize("ingredient_data, expected_price", [
        ([("FILLING", "Cheese", 50.0), ("SAUCE", "Ketchup", 20.0)], 270.0),
        ([("FILLING", "Lettuce", 10.0), ("FILLING", "Tomato", 15.0)], 225.0),
    ])
    def test_get_receipt_parametrized(self, make_burger, bun, ingredient, ingredient_data, expected_price):
        burger = make_burger()
        bun = bun(name="Classic", price=100.0)
        burger.set_buns(bun)
        for type_, name, price in ingredient_data:
            ing = ingredient(type_=type_, name=name, price=price)
            burger.add_ingredient(ing)

        assert burger.get_price() == expected_price

    def test_get_price(self, make_burger, bun, ingredient):
        burger = make_burger()
        bun = bun(name="Sesame", price=80.0)
        ing1 = ingredient(type_="FILLING", name="Cheese", price=50.0)
        ing2 = ingredient(type_="SAUCE", name="Ketchup", price=20.0)

        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        expected = bun.get_price() * 2 + ing1.get_price() + ing2.get_price()
        assert burger.get_price() == expected