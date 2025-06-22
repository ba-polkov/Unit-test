import pytest
from praktikum import praktikum
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_database_returns_buns_and_ingredients(self):
        db = Database()
        buns = db.available_buns()
        ingredients = db.available_ingredients()

        assert len(buns) == 3
        assert all(bun.get_name() for bun in buns)
        assert all(bun.get_price() >= 0 for bun in buns)

        assert len(ingredients) == 6
        assert all(i.get_price() >= 0 for i in ingredients)
        assert set(i.get_type() for i in ingredients) == {INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING}

    @pytest.mark.parametrize(
        "ingredients_list, expected_ingredients, expected_price",
        [
            (
                [
                    Ingredient(INGREDIENT_TYPE_SAUCE,   "sauce 0",    5),
                    Ingredient(INGREDIENT_TYPE_SAUCE,   "hot sauce",  10),
                    Ingredient(INGREDIENT_TYPE_FILLING, "filling 0",  15),
                    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur",   60),
                    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet",     50),
                    Ingredient(INGREDIENT_TYPE_FILLING, "sausage",    60),
                ],
                ["hot sauce", "dinosaur", "cutlet"],
                320
            ),

            (
                [
                    Ingredient(INGREDIENT_TYPE_SAUCE,   "hot sauce",  10),
                    Ingredient(INGREDIENT_TYPE_SAUCE,   "sauce 0",     5),
                    Ingredient(INGREDIENT_TYPE_FILLING, "filling 0",  15),
                    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur",   60),
                    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet",     50),
                    Ingredient(INGREDIENT_TYPE_FILLING, "sausage",    60),
                ],
                ["sauce 0", "dinosaur", "cutlet"],
                315
            ),
        ],
        ids=["with‑hot‑sauce", "with‑sauce‑0"]
    )

    def test_main_with_mocked_db(self, monkeypatch, capsys, mocked_database, ingredients_list, expected_ingredients, expected_price):
        mocked_database.available_ingredients.return_value = ingredients_list
        monkeypatch.setattr("praktikum.praktikum.Database", lambda: mocked_database)

        praktikum.main()
        captured = capsys.readouterr().out

        for ing_name in expected_ingredients:
            assert ing_name in captured

        assert "sausage" not in captured
        assert "mock bun" in captured
        assert f"Price: {expected_price}" in captured
