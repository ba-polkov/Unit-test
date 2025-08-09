from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDB:

    def test_database_available_buns_length(self):
        """
        Проверяет длину списка булок в базе данных
        """
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_database_available_buns_first_name(self):
        """
        Проверяет имя первой булки в базе данных
        """
        db = Database()
        buns = db.available_buns()
        assert buns[0].get_name() == "black bun"

    def test_database_available_buns_first_price(self):
        """
        Проверяет цену первой булки в базе данных
        """
        db = Database()
        buns = db.available_buns()
        assert buns[0].get_price() == 100

    def test_database_available_buns_second_name(self):
        """
        Проверяет имя второй булки в базе данных
        """
        db = Database()
        buns = db.available_buns()
        assert buns[1].get_name() == "white bun"

    def test_database_available_buns_second_price(self):
        """
        Проверяет цену второй булки в базе данных
        """
        db = Database()
        buns = db.available_buns()
        assert buns[1].get_price() == 200

    def test_database_available_buns_third_name(self):
        """
        Проверяет имя третьей булки в базе данных
        """
        db = Database()
        buns = db.available_buns()
        assert buns[2].get_name() == "red bun"

    def test_database_available_buns_third_price(self):
        """
        Проверяет цену третьей булки в базе данных
        """
        db = Database()
        buns = db.available_buns()
        assert buns[2].get_price() == 300

    def test_database_available_ingredients_length(self):
        """
        Проверяет длину списка ингредиентов в базе данных
        """
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_database_available_ingredients_sauce_types(self):
        """
        Проверяет типы первых трех ингредиентов (соусы)
        """
        db = Database()
        ingredients = db.available_ingredients()
        for i in range(3):
            assert ingredients[i].get_type() == INGREDIENT_TYPE_SAUCE

    def test_database_available_ingredients_filling_types(self):
        """
        Проверяет типы последних трех ингредиентов (начинки)
        """
        db = Database()
        ingredients = db.available_ingredients()
        for i in range(3, 6):
            assert ingredients[i].get_type() == INGREDIENT_TYPE_FILLING

    def test_database_available_ingredients_first_name(self):
        """
        Проверяет имя первого ингредиента (соуса)
        """
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"

    def test_database_available_ingredients_first_price(self):
        """
        Проверяет цену первого ингредиента (соуса)
        """
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[0].get_price() == 100

    def test_database_available_ingredients_fourth_name(self):
        """
        Проверяет имя четвертого ингредиента (начинки)
        """
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[3].get_name() == "cutlet"

    def test_database_available_ingredients_third_price(self):
        """
        Проверяет цену третьего ингредиента (соуса)
        """
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[2].get_price() == 300

    def test_database_available_ingredients_sixth_price(self):
        """
        Проверяет цену шестого ингредиента (начинки)
        """
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[5].get_price() == 300