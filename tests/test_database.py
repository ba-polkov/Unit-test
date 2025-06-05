from data import BUNS_DATA, FILLINGS_DATA, SAUCES_DATA

class TestDatabase:

    def test_initial_buns_count(self, database):
        # тест проверяет, что при инициализации база данных содержит 3 булки
        assert len(database.available_buns()) == 3

    def test_initial_ingredients_count(self, database):
        # тест проверяет, что при инициализации база данных содержит 6 ингредиентов (3 соуса + 3 начинки)
        assert len(database.available_ingredients()) == 6

    def test_available_buns(self, database):
        buns = database.available_buns()
        actual_names_and_prices = [(bun.name, bun.price) for bun in buns]
        expected_names_and_prices = set((name, price) for name, price in BUNS_DATA)
        assert set(actual_names_and_prices) == expected_names_and_prices

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        expected_ingredients = SAUCES_DATA + FILLINGS_DATA
        actual_ingredients_set = {(ingr.name, ingr.type, ingr.price) for ingr in ingredients}
        expected_ingredients_set = set((iname, itype, iprice) for iname, iprice, itype in expected_ingredients)
        assert actual_ingredients_set == expected_ingredients_set