import pytest


class TestBurger:
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ing_1):
        burger.add_ingredient(mock_ing_1)
        assert mock_ing_1 in burger.ingredients

    def test_remove_ingredient(self, burger, mock_ing_1):
        burger.add_ingredient(mock_ing_1)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    @pytest.mark.parametrize("start_index,new_index", [
        (0, 1),
        (1, 0),
    ])
    def test_move_ingredient(self, burger, mock_ing_1, mock_ing_2, start_index, new_index):
        ingredient1 = mock_ing_1
        ingredient2 = mock_ing_2
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(start_index, new_index)
        assert burger.ingredients[new_index] == [ingredient1, ingredient2][start_index]

    @pytest.mark.parametrize(
        "bun_price, ingredient_price",
        [
            (100, 200),
            (150, 250),
            (200, 300),
        ]
    )
    def test_get_price_1(self, burger, mock_bun, mock_ing_1, bun_price, ingredient_price):
        mock_bun.get_price.return_value = bun_price
        mock_ing_1.get_price.return_value = ingredient_price
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_1)
        expected_price = bun_price * 2 + ingredient_price
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, mock_bun, mock_ing_1):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ing_1)
        receipt = burger.get_receipt()
        assert "(==== red bun ====)" in receipt
        assert "= filling dinosaur =" in receipt.lower()
        assert "Price: 800" in receipt
