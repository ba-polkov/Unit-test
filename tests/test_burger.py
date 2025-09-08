import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def make_burger_with_bun(name="black bun", price=100):
    b = Burger()
    b.set_buns(Bun(name, price))
    return b


@pytest.mark.unit
def test_set_buns_changes_price():
    b = make_burger_with_bun("black bun", 100)
    assert b.get_price() == 200

    b.set_buns(Bun("white bun", 250))
    assert b.get_price() == 500


@pytest.mark.unit
def test_add_and_remove_ingredients():
    b = make_burger_with_bun()

    ketchup = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 50)
    cutlet = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 300)

    b.add_ingredient(ketchup)
    b.add_ingredient(cutlet)

    assert [i.get_name() for i in b.ingredients] == ["ketchup", "cutlet"]

    b.remove_ingredient(0)
    assert [i.get_name() for i in b.ingredients] == ["cutlet"]


@pytest.mark.unit
def test_move_ingredient_reorders():
    b = make_burger_with_bun()
    a = Ingredient(INGREDIENT_TYPE_SAUCE, "a", 10)
    c = Ingredient(INGREDIENT_TYPE_FILLING, "c", 30)
    b.add_ingredient(a)
    b.add_ingredient(c)

    # переставим c на позицию 0
    b.move_ingredient(1, 0)
    assert [i.get_name() for i in b.ingredients] == ["c", "a"]


@pytest.mark.unit
def test_total_price_includes_bun_and_ingredients():
    b = make_burger_with_bun(price=120)
    b.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "sauce", 50))
    b.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "filling", 300))
    assert b.get_price() == 240 + 50 + 300


@pytest.mark.unit
def test_get_receipt_contains_buns_ingredients_and_price():
    b = make_burger_with_bun("sesame", 150)
    b.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "bbq", 60))
    receipt = b.get_receipt().lower()

    assert "sesame" in receipt
    assert "bbq" in receipt
    assert str(b.get_price()) in receipt


@pytest.mark.unit
def test_remove_ingredient_out_of_range_is_safe():
    b = make_burger_with_bun()
    b.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "x", 10))
    before = list(b.ingredients)
    try:
        b.remove_ingredient(5)
        after = list(b.ingredients)
        assert before == after
    except IndexError:
        assert True
