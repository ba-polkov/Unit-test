import allure
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from allure_commons.types import Severity

@allure.story("Тесты для класса Burger")
class TestBurger:

    @allure.title("Добавление булочки в бургер")
    def test_set_buns(self, burger, mock_bun):
        with allure.step("Добавляем булочку в бургер"):
            burger.set_buns(mock_bun)

        with allure.step("Проверяем что булочка установлена"):
            assert burger.bun == mock_bun

    @allure.title("Добавление ингредиента в бургер")
    @allure.severity(Severity.CRITICAL)
    def test_add_ingredient(self, burger, mock_sauce):
        with allure.step("Добавляем ингредиент в бургер"):
            burger.add_ingredient(mock_sauce)

        with allure.step("Проверяем что ингредиент добавлен"):
            assert len(burger.ingredients) == 1
            assert mock_sauce in burger.ingredients

    @allure.title("Удаление ингредиента из бургера")
    @allure.severity(Severity.CRITICAL)
    def test_remove_ingredient(self, burger, mock_sauce, mock_filling):
        with allure.step("Добавляем два ингредиента в бургер"):
            burger.add_ingredient(mock_sauce)
            burger.add_ingredient(mock_filling)

        with allure.step("Удаляем первый ингредиент"):
            burger.remove_ingredient(0)

        with allure.step("Проверяем что остался только второй ингредиент"):
            assert len(burger.ingredients) == 1
            assert mock_filling in burger.ingredients

    @allure.title("Перемещение ингредиента в бургере")
    @allure.severity(Severity.NORMAL)
    @pytest.mark.parametrize('initial_index,new_index,expected_order', [
        (0, 1, [1, 0, 2]),
        (1, 0, [1, 0, 2]),
        (2, 1, [0, 2, 1])
    ])
    def test_move_ingredient(self, burger, initial_index, new_index, expected_order):
        with allure.step(f"Подготавливаем тестовые данные: {initial_index}->{new_index}"):
            mock_ingredients = [Mock(), Mock(), Mock()]
            burger.ingredients = mock_ingredients.copy()

        with allure.step(f"Перемещаем ингредиент с позиции {initial_index} на {new_index}"):
            burger.move_ingredient(initial_index, new_index)

        with allure.step("Проверяем новый порядок ингредиентов"):
            assert burger.ingredients == [mock_ingredients[i] for i in expected_order]

    @allure.title("Расчет цены бургера только с булочкой")
    @allure.severity(Severity.CRITICAL)
    def test_get_price_with_only_bun(self, burger, mock_bun):
        with allure.step("Добавляем булочку в бургер"):
            burger.set_buns(mock_bun)

        with allure.step("Проверяем расчет цены (должна быть 200)"):
            assert burger.get_price() == 200.0  # 100 * 2 (две булочки)

    @allure.title("Расчет цены бургера с булочкой и ингредиентами")
    @allure.severity(Severity.CRITICAL)
    def test_get_price_with_bun_and_ingredients(self, prepared_burger):
        with allure.step("Проверяем расчет цены (должна быть 325)"):
            # 100*2 (булочки) + 50 (соус) + 75 (начинка) = 325
            assert prepared_burger.get_price() == 325.0

    @allure.title("Генерация чека для бургера только с булочкой")
    @allure.severity(Severity.NORMAL)
    def test_get_receipt_with_only_bun(self, burger, bun):
        with allure.step("Добавляем булочку в бургер"):
            burger.set_buns(bun)

        with allure.step("Генерируем чек"):
            receipt = burger.get_receipt()

        with allure.step("Проверяем содержание чека"):
            assert "(==== white bun ====)" in receipt
            assert "(==== white bun ====)\n" in receipt
            assert "Price: 400" in receipt

    @allure.title("Генерация чека для полного бургера")
    @allure.severity(Severity.NORMAL)
    def test_get_receipt_with_bun_and_ingredients(self, prepared_burger):
        with allure.step("Генерируем чек и разбиваем на строки"):
            receipt = prepared_burger.get_receipt()
            lines = receipt.split('\n')

        with allure.step("Проверяем содержание чека"):
            assert lines[0] == "(==== black bun ====)"
            assert lines[1] == "= sauce hot sauce ="
            assert lines[2] == "= filling cutlet ="
            assert lines[3] == "(==== black bun ====)"
            assert lines[4] == ""
            assert "Price: 325" in lines[5]

    @allure.title("Попытка удаления несуществующего ингредиента")
    @allure.severity(Severity.MINOR)
    def test_remove_nonexistent_ingredient_raises_exception(self, burger):
        with allure.step("Пытаемся удалить несуществующий ингредиент"):
            with pytest.raises(IndexError):
                burger.remove_ingredient(0)

        with allure.step("Добавляем один ингредиент и пытаемся удалить второй"):
            mock_ingredient = Mock()
            burger.add_ingredient(mock_ingredient)
            with pytest.raises(IndexError):
                burger.remove_ingredient(1)