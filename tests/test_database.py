import allure
from data import Data
from conftest import *
from praktikum.database import Database
import pytest



class TestDataBase:
    @pytest.mark.parametrize('buns_number, buns_name, buns_price', Data.buns_data_for_test_database)
    def test_avalable_buns_database(self, data_base_fixture,buns_number, buns_name, buns_price):
        test_buns = data_base_fixture.available_buns()
        assert test_buns[buns_number].get_name() == buns_name
        assert test_buns[buns_number].get_price() == buns_price
