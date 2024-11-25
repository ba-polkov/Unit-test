from src.database import Database


class TestDataBase:
    def test_data_base_bun_init(self):
        db = Database()
        expected_result = ["black bun", "white bun", "red bun"]
        actual_result = [bun.name for bun in db.available_buns()]
        assert expected_result == actual_result

    def test_data_base_ingredients_init(self):
        db = Database()
        expected_result = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        actual_result = [ingredient.name for ingredient in db.available_ingredients()]
        assert expected_result == actual_result

    def test_data_base_bun_prices_init(self):
        db = Database()
        expected_result = [100, 200, 300]
        actual_result = [bun.price for bun in db.available_buns()]
        assert expected_result == actual_result

    def test_data_base_ingredients_prices_init(self):
        db = Database()
        expected_result = [100, 200, 300, 100, 200, 300]
        actual_result = [bun.price for bun in db.available_ingredients()]
        assert expected_result == actual_result
