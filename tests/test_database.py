import pytest
import allure
from data import TestDataDB


class TestDatabase:
    @allure.title("Проверка инициализации базы данных")
    @allure.description("Проверяем, что база данных содержит правильное количество булок и ингредиентов")
    def test_initialization(self, db):
        assert len(db.available_buns()) == 3, "Должно быть 3 булки в базе данных"
        assert len(db.available_ingredients()) == 6, "Должно быть 6 ингредиентов в базе данных"

    @allure.title("Проверка работы метода available_buns")
    @allure.description("Через параметризацию проверяем имя и стоимость каждой булки")
    @pytest.mark.parametrize("bun_index, expected_name, expected_price", TestDataDB.test_data_buns)
    def test_available_buns(self, db, bun_index, expected_name, expected_price):
        # ACT
        buns = db.available_buns()
        actual_bun = buns[bun_index]
        
        # ASSERT
        assert actual_bun.name == expected_name, f"Неверное имя булки по индексу {bun_index}"
        assert actual_bun.price == expected_price, f"Неверная цена булки по индексу {bun_index}"

    @allure.title("Проверка работы метода available_ingredients")
    @allure.description("Через параметризацию проверяем тип, имя и стоимость ингредиентов")
    @pytest.mark.parametrize("ing_index, expected_type, expected_name, expected_price", TestDataDB.test_data_ingredients)
    def test_available_ingredients(self, db, ing_index, expected_type, expected_name, expected_price):
        # ACT
        ingredients = db.available_ingredients()
        actual_ingredient = ingredients[ing_index]
        
        # ASSERT
        assert actual_ingredient.type == expected_type, f"Неверный тип ингредиента по индексу {ing_index}"
        assert actual_ingredient.name == expected_name, f"Неверное название ингредиента по индексу {ing_index}"
        assert actual_ingredient.price == expected_price, f"Неверная цена ингредиента по индексу {ing_index}"