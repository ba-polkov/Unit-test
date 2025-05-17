from practicum.database import Database
from practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import names_from_buns, ingredient_names_by_type


class TestDatabase:
    def test_available_buns(self):
        db = Database()
        names = names_from_buns(db.available_buns())
        assert names == ["black bun", "white bun", "red bun"], "Список булок не корректный"

    def test_available_ingredients(self, database):
        db = Database()
        ingredients = db.available_ingredients()

        sauces = ingredient_names_by_type(ingredients, INGREDIENT_TYPE_SAUCE)
        fillings = ingredient_names_by_type (ingredients, INGREDIENT_TYPE_FILLING)

        assert sauces == ["hot sauce", "sour cream", "chili sauce"], "Соусы не совпадают"
        assert fillings == ["cutlet", "dinosaur", "sausage"], "Начинки не совпадают"