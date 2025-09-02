from unittest.mock import MagicMock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_price_with_only_bun(empty_burger):
    # цена бургера только с булкой = цена булки * 2
    assert empty_burger.get_price() == 200  # если цена булки 100


def test_add_remove_ingredient_affects_price_and_list(empty_burger):
    # создаем ингредиенты
    ing1 = MagicMock()
    ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ing1.get_name.return_value = "ketchup"
    ing1.get_price.return_value = 10

    ing2 = MagicMock()
    ing2.get_type.return_value = INGREDIENT_TYPE_FILLING
    ing2.get_name.return_value = "cutlet"
    ing2.get_price.return_value = 100

    # добавили
    empty_burger.add_ingredient(ing1)
    empty_burger.add_ingredient(ing2)
    assert len(empty_burger.ingredients) == 2
    assert empty_burger.get_price() == 310  # 100*2 + 10 + 100

    # удалили первый ингредиент
    empty_burger.remove_ingredient(0)
    assert len(empty_burger.ingredients) == 1
    assert empty_burger.ingredients[0].get_name() == "cutlet"


def test_move_ingredient_changes_order(empty_burger):
    ing1 = MagicMock()
    ing1.get_name.return_value = "ketchup"
    ing2 = MagicMock()
    ing2.get_name.return_value = "cutlet"
    ing3 = MagicMock()
    ing3.get_name.return_value = "mayo"

    empty_burger.add_ingredient(ing1)
    empty_burger.add_ingredient(ing2)
    empty_burger.add_ingredient(ing3)

    empty_burger.move_ingredient(2, 0)
    names = [i.get_name() for i in empty_burger.ingredients]
    assert names == ["mayo", "ketchup", "cutlet"]


def test_get_receipt_contains_expected_lines(empty_burger):
    ing1 = MagicMock()
    ing1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ing1.get_name.return_value = "ketchup"
    ing1.get_price.return_value = 10

    ing2 = MagicMock()
    ing2.get_type.return_value = INGREDIENT_TYPE_FILLING
    ing2.get_name.return_value = "cutlet"
    ing2.get_price.return_value = 100

    empty_burger.add_ingredient(ing1)
    empty_burger.add_ingredient(ing2)

    receipt = empty_burger.get_receipt()
    assert "(==== black bun ====)" in receipt
    assert "ketchup" in receipt
    assert "cutlet" in receipt
    assert "Price: 310" in receipt
