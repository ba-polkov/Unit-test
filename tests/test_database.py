import pytest
from tests.data import ExpectedBunNames, ExpectedIngredientNames

class TestDatabase:

    @pytest.mark.parametrize("expected_bun_names", ExpectedBunNames.data)
    def test_available_buns(self, database, expected_bun_names):
        buns = database.available_buns()
        assert len(buns) == len(expected_bun_names) and all(
        bun.get_name() == expected_name for bun, expected_name in zip(buns, expected_bun_names)
        )

    @pytest.mark.parametrize("expected_ingredient_names", ExpectedIngredientNames.data)
    def test_available_ingredients(self, database, expected_ingredient_names):
        ingredients = database.available_ingredients()
        assert len(ingredients) == len(expected_ingredient_names) and all(
        ingredient.get_name() == expected_name for ingredient, expected_name in zip(ingredients, expected_ingredient_names)
        )
