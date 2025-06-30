import pytest
from practicum.burger import Burger

class TestBurger:
    def test_set_buns(self, empty_burger, mock_bun):
        empty_burger.set_buns(mock_bun)
        assert empty_burger.bun == mock_bun

    def test_add_ingredient(self, empty_burger, mock_ingredient_sauce):
        empty_burger.add_ingredient(mock_ingredient_sauce)
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == mock_ingredient_sauce

    def test_remove_ingredient(self, prepared_burger, mock_ingredients):
        prepared_burger.remove_ingredient(0)
        assert len(prepared_burger.ingredients) == 1
        assert prepared_burger.ingredients[0] == mock_ingredients[1]

    @pytest.mark.parametrize("index_from,index_to", [(0, 1), (1, 0)])
    def test_move_ingredient(self, prepared_burger, index_from, index_to):
        moved_ingredient = prepared_burger.ingredients[index_from]
        prepared_burger.move_ingredient(index_from, index_to)
        assert prepared_burger.ingredients[index_to] == moved_ingredient

    def test_get_price(self, prepared_burger, mock_bun, mock_ingredients):
        expected_price = (mock_bun.get_price() * 2 + 
                         sum(ing.get_price() for ing in mock_ingredients))
        assert prepared_burger.get_price() == expected_price

    def test_get_receipt(self, prepared_burger, mock_bun, mock_ingredient_sauce):
        receipt = prepared_burger.get_receipt()
        assert f"(==== {mock_bun.get_name()} ====)" in receipt
        assert f"= {mock_ingredient_sauce.get_type().lower()} {mock_ingredient_sauce.get_name()} =" in receipt
        assert f"Price: {prepared_burger.get_price()}" in receipt