import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from allure_commons.types import Severity


@allure.feature("Ingredient")
@allure.story("Тесты для класса Ingredient")
class TestIngredient:

    @allure.title("Проверка создания ингредиента")
    @allure.severity(Severity.BLOCKER)
    def test_ingredient_creation(self):
        with allure.step("Создаем ингредиент типа соус"):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

        with allure.step("Проверяем корректность установки атрибутов"):
            assert ingredient.type == INGREDIENT_TYPE_SAUCE
            assert ingredient.name == "hot sauce"
            assert ingredient.price == 100

    @allure.title("Проверка метода get_price()")
    @allure.severity(Severity.CRITICAL)
    def test_get_price(self):
        with allure.step("Создаем ингредиент с ценой 200"):
            ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)

        with allure.step("Проверяем возвращаемое значение get_price()"):
            assert ingredient.get_price() == 200

    @allure.title("Проверка метода get_name()")
    @allure.severity(Severity.CRITICAL)
    def test_get_name(self):
        with allure.step("Создаем ингредиент с именем 'sour cream'"):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 150)

        with allure.step("Проверяем возвращаемое значение get_name()"):
            assert ingredient.get_name() == "sour cream"

    @allure.title("Проверка метода get_type()")
    @allure.severity(Severity.CRITICAL)
    def test_get_type(self):
        with allure.step("Создаем ингредиент типа начинка"):
            ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 300)

        with allure.step("Проверяем возвращаемое значение get_type()"):
            assert ingredient.get_type() == INGREDIENT_TYPE_FILLING