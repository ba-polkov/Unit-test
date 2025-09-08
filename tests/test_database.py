import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.unit
def test_available_buns_and_ingredients_not_empty_and_types():
    db = Database()
    buns = db.available_buns()
    ings = db.available_ingredients()

    assert isinstance(buns, list)
    assert isinstance(ings, list)
    assert buns, "Ожидается хотя бы одна булка"
    assert ings, "Ожидается хотя бы один ингредиент"

    assert all(isinstance(b, Bun) for b in buns)
    assert all(isinstance(i, Ingredient) for i in ings)


@pytest.mark.unit
def test_known_items_exist_soft_check():
    db = Database()
    bun_names = {b.get_name() for b in db.available_buns()}
    ing_names = {i.get_name() for i in db.available_ingredients()}

    assert "black bun" in bun_names

    expected_some = {"hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"}
    assert expected_some & ing_names, "Должен присутствовать хотя бы один из ожидаемых ингредиентов"


@pytest.mark.unit
def test_ingredients_have_valid_types_and_positive_prices():
    db = Database()
    for ing in db.available_ingredients():
        assert ing.get_type() in (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING)
        assert isinstance(ing.get_price(), (int, float))
        assert ing.get_price() >= 0
        assert isinstance(ing.get_name(), str) and ing.get_name()


@pytest.mark.unit
def test_available_methods_return_consistent_data():
    db = Database()
    buns1 = db.available_buns()
    buns2 = db.available_buns()
    ings1 = db.available_ingredients()
    ings2 = db.available_ingredients()

    assert [b.get_name() for b in buns1] == [b.get_name() for b in buns2]
    assert [i.get_name() for i in ings1] == [i.get_name() for i in ings2]
