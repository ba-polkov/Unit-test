from data import TestDataBase
from conftest import db
import pytest


class TestDatabase:

    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.test_database_buns)
    def test_buns_database(self, db, index_bun, bun_name, bun_price):
        data_buns = db.available_buns()
        assert data_buns[index_bun].get_name() == bun_name and data_buns[index_bun].get_price() == bun_price


    @pytest.mark.parametrize('index_i, type_ingredient, name_ingredient, price_ingredient', TestDataBase.test_database_ingredients)
    def test_ingredients_database(self, db, index_i, type_ingredient, name_ingredient, price_ingredient):
        data_ingredients = db.available_ingredients()
        assert (data_ingredients[index_i].get_name() == name_ingredient and
                data_ingredients[index_i].get_type() == type_ingredient and
                data_ingredients[index_i].get_price() == price_ingredient)