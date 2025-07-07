import pytest
from praktikum.database import Database

from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    # проверяем название булочки и ее цену для  бд
    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ],
    )
    def test_bun_name_and_price_bd(self, index, expected_name, expected_price):
        db = Database()
        bun = db.available_buns()[index]
        assert bun.get_name() == expected_name and bun.get_price() == expected_price

    @pytest.mark.parametrize(
        "index,expected_type,  expected_name, expected_price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ],
    )
    def test_ingredient_all_param_bd(
        self, index, expected_type, expected_name, expected_price
    ):
        db = Database()
        ingredient = db.available_ingredients()[index]
        assert (
            ingredient.get_name() == expected_name
            and ingredient.get_price() == expected_price
            and ingredient.get_type() == expected_type
        )
