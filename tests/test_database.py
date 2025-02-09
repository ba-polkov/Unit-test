import pytest
from praktikum.database import Database


class TestDatabase:
    @pytest.mark.parametrize('bun_index,bun_name', [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun"),
    ])
    def test_available_buns(self, bun_index, bun_name):
        db = Database()
        db_buns = db.available_buns()
        assert len(db_buns) == 3

        assert db_buns[bun_index].name == bun_name

    @pytest.mark.parametrize('ingr_index,ingr_name',[
        (0, "hot sauce"),
        (1, "sour cream"),
        (3, "cutlet"),
        (4, "dinosaur")
    ])
    def test_available_ingredients(self, ingr_index, ingr_name):
        db = Database()
        db_ingr = db.available_ingredients()
        assert len(db_ingr) == 6

        assert db_ingr[ingr_index].name == ingr_name
