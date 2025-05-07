import pytest
import allure
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    """Фикстура для создания пустого бургера."""
    return Burger()


@pytest.fixture
def bun():
    """Фикстура для создания булочки."""
    return Bun("black bun", 100)


@pytest.fixture
def ingredient_sauce():
    """Фикстура для создания соуса."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)


@pytest.fixture
def ingredient_filling():
    """Фикстура для создания начинки."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)


@allure.feature("Бургер")
@allure.story("Установка булочки и добавление ингредиентов")
class TestBurger:
    @allure.title("Тест на установку булочки для бургера")
    def test_set_buns(self, burger, bun):
        """Тест на установку булочки для бургера."""
        with allure.step("Устанавливаем булочку для бургера"):
            burger.set_buns(bun)

        with allure.step("Проверяем имя и цену булочки"):
            assert burger.bun.get_name() == "black bun"
            assert burger.bun.get_price() == 100

    @allure.title("Тест на добавление ингредиента в бургер")
    def test_add_ingredient(self, burger, ingredient_sauce):
        """Тест на добавление ингредиента в бургер."""
        with allure.step("Добавляем соус в бургер"):
            burger.add_ingredient(ingredient_sauce)

        with allure.step("Проверяем количество ингредиентов и их данные"):
            assert len(burger.ingredients) == 1
            assert burger.ingredients[0].get_name() == "hot sauce"
            assert burger.ingredients[0].get_price() == 50

    @allure.title("Тест на удаление ингредиента из бургера")
    def test_remove_ingredient(self, burger, ingredient_sauce):
        """Тест на удаление ингредиента из бургера."""
        with allure.step("Добавляем соус в бургер"):
            burger.add_ingredient(ingredient_sauce)

        with allure.step("Удаляем ингредиент из бургера"):
            burger.remove_ingredient(0)

        with allure.step("Проверяем, что ингредиентов больше нет"):
            assert len(burger.ingredients) == 0

    @allure.title("Тест на перемещение ингредиента в бургер")
    def test_move_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        """Тест на перемещение ингредиента в бургер."""
        with allure.step("Добавляем соус и начинку в бургер"):
            burger.add_ingredient(ingredient_sauce)
            burger.add_ingredient(ingredient_filling)

        with allure.step("Перемещаем ингредиенты"):
            burger.move_ingredient(1, 0)

        with allure.step("Проверяем правильность порядка ингредиентов"):
            assert burger.ingredients[0].get_name() == "cutlet"
            assert burger.ingredients[1].get_name() == "hot sauce"

    @allure.title("Тест на расчет цены бургера")
    def test_get_price(self, burger, bun, ingredient_sauce, ingredient_filling):
        """Тест на расчет цены бургера."""
        with allure.step("Устанавливаем булочку и добавляем ингредиенты"):
            burger.set_buns(bun)
            burger.add_ingredient(ingredient_sauce)
            burger.add_ingredient(ingredient_filling)

        with allure.step("Проверяем расчет цены"):
            assert burger.get_price() == 400  # 2 * 100 (булочка) + 50 (соус) + 150 (начинка)

    @allure.title("Тест на генерацию чека для бургера")
    def test_get_receipt(self, burger, bun, ingredient_sauce, ingredient_filling):
        """Тест на генерацию чека для бургера."""
        with allure.step("Устанавливаем булочку и добавляем ингредиенты"):
            burger.set_buns(bun)
            burger.add_ingredient(ingredient_sauce)
            burger.add_ingredient(ingredient_filling)

        with allure.step("Генерируем и проверяем чек"):
            receipt = burger.get_receipt()
            assert "Price: 400" in receipt
            assert "(==== black bun ====)" in receipt
            assert "= sauce hot sauce =" in receipt
            assert "= filling cutlet =" in receipt