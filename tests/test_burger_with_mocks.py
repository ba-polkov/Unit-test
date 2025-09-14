import pytest
from praktikum.burger import Burger

@pytest.mark.unit
def test_get_price_and_receipt_with_mocks(mock_bun, mock_ingredient_filling, mock_ingredient_sauce):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_filling)
    burger.add_ingredient(mock_ingredient_sauce)

    # ожидаемая цена = 2 * булка + начинка + соус
    expected_price = (
        mock_bun.get_price() * 2
        + mock_ingredient_filling.get_price()
        + mock_ingredient_sauce.get_price()
    )
    assert burger.get_price() == expected_price

    receipt = burger.get_receipt()
    # проверяем, что чек включает все позиции
    assert "(==== Sesame ====)" in receipt
    assert "= filling Beef =" in receipt
    assert "= sauce Ketchup =" in receipt
    assert f"Price: {expected_price}" in receipt
