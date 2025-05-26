import allure

from praktikum.database import Database

class TestClassDatabase:
    @allure.title('Добавление в базу данных 3 булок')
    def test_added_three_buns_in_database(self):
        data_base = Database()
        assert len(data_base.available_buns()) == 3

    @allure.title('Добавление в базу данных 6 ингредиентов')
    def test_added_six_ingredients_in_database(self):
        data_base = Database()
        assert len(data_base.available_ingredients()) == 6