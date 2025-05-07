import pytest
import allure
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def database():
    """Создаем экземпляр базы данных для тестов."""
    return Database()


@allure.feature("База данных")
@allure.story("Доступные булочки")
class TestDatabase:
    @allure.title("Проверка метода available_buns()")
    def test_available_buns(self, database):
        """Проверка метода available_buns()"""

        with allure.step("Получаем список булочек из базы данных"):
            buns = database.available_buns()

        with allure.step("Проверяем, что возвращается список булочек"):
            assert isinstance(buns, list), "Ожидался список булочек"
            assert len(buns) == 3, "Ожидалось 3 булочки"

        with allure.step("Проверяем, что каждый элемент списка является экземпляром класса Bun"):
            assert all(isinstance(bun, Bun) for bun in buns), "Не все элементы списка являются булочками (Bun)"

        with allure.step("Проверяем правильность данных"):
            assert buns[0].get_name() == "black bun", "Имя первой булочки неверное"
            assert buns[1].get_price() == 200, "Цена второй булочки неверная"

    @allure.title("Проверка метода available_ingredients()")
    def test_available_ingredients(self, database):
        """Проверка метода available_ingredients()"""

        with allure.step("Получаем список ингредиентов из базы данных"):
            ingredients = database.available_ingredients()

        with allure.step("Проверяем, что возвращается список ингредиентов"):
            assert isinstance(ingredients, list), "Ожидался список ингредиентов"
            assert len(ingredients) == 6, "Ожидалось 6 ингредиентов"

        with allure.step("Проверяем, что каждый элемент списка является экземпляром класса Ingredient"):
            assert all(isinstance(ingredient, Ingredient) for ingredient in
                       ingredients), "Не все элементы списка являются ингредиентами (Ingredient)"

        with allure.step("Проверяем правильность данных"):
            assert ingredients[0].get_name() == "hot sauce", "Имя первого ингредиента неверное"
            assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING, "Тип четвертого ингредиента неверный"
            assert ingredients[5].get_price() == 300, "Цена последнего ингредиента неверная"