from Diplom_1.practicum import Database
from Diplom_1.practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        names = [bun.get_name()for bun in db.available_buns()]
        assert names == ["black bun", "white bun", "red bun"], "Список булок не корректный"

    def test_available_ingredients(self, database):
        db = Database()
        ingredients = db.available_ingredients()

        sauces = [i.get_name() for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [i.get_name() for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

        assert sauces == ["hot sauce", "sour cream", "chili sauce"], "Соусы не совпадают"
        assert fillings == ["cutlet", "dinosaur", "sausage"], "Начинки не совпадают"
