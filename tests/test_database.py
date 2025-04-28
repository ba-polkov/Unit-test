import pytest
from mock_data import MockData
from src.database import Database

class TestDataBase:

    @pytest.mark.parametrize('bun_ind, available_bun_name', [
        (0, MockData.BLACK_BUN),
        (1, MockData.WHITE_BUN),
        (2, MockData.RED_BUN)
    ])
    def test_available_buns_in_the_database_and_exist_in_list(self, bun_ind: int, available_bun_name: str):
        db = Database()
        assert db.available_buns()[bun_ind].name == available_bun_name

    @pytest.mark.parametrize('ingredient_ind, available_ingredient_name', [
        (0, MockData.HOT_SAUCE),
        (1, MockData.SOUR_CREAM),
        (2, MockData.CHILI_SAUCE),
        (3, MockData.CUTLET_FILLING),
        (4, MockData.DINOSAUR_FILLING),
        (5, MockData.SAUSAGE_FILLING)
    ])
    def test_available_ingredients_in_the_database_and_exist_in_list(self, ingredient_ind: int, available_ingredient_name: str):
        db = Database()
        assert db.available_ingredients()[ingredient_ind].name == available_ingredient_name
