from helpers import TestTools
from praktikum.database import Database


class TestDatabase:

    def test_database_available_buns_return_available_buns(self):
        database = Database()
        buns_from_database = []
        for element in database.buns:
            buns_from_database.append((element.name, element.price))
        buns_from_method = []
        for element in database.available_buns():
            buns_from_method.append((element.name, element.price))
        TestTools.check_unit_test_result(expected_value=buns_from_database, actually_value=buns_from_method)

    def test_database_available_ingredients_return_available_ingredients(self):
        database = Database()
        ingredients_from_database = []
        for element in database.ingredients:
            ingredients_from_database.append((element.type, element.name, element.price))
        ingredients_from_method = []
        for element in database.available_ingredients():
            ingredients_from_method.append((element.type, element.name, element.price))
        TestTools.check_unit_test_result(expected_value=ingredients_from_database, actually_value=ingredients_from_method)