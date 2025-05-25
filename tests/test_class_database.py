import allure

from conftest import create_test_database

class TestClassDatabase:
    @allure.title('Добавление в базу данных 3 булок')
    def test_added_three_buns_in_database(self, create_test_database):
        assert len(create_test_database.available_buns()) == 3

    @allure.title('Добавление в базу данных 6 ингредиентов')
    def test_added_six_ingredients_in_database(self, create_test_database):
        assert len(create_test_database.available_ingredients()) == 6