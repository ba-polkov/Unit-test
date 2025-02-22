import pytest
from praktikum.praktikum import Burger
from unittest.mock import Mock, patch

class TestBurger:
    # Проверяем, что при создании бургера булка отсутствует
    def test_initial_bun_is_none(self):
        burger = Burger()
        assert burger.bun is None

    # Проверяем, что при создании бургера список ингредиентов пуст
    def test_initial_ingredients_is_empty_list(self):
        burger = Burger()
        assert burger.ingredients == []

    # Проверяем, что булка устанавливается корректно
    @patch("praktikum.bun.Bun")
    def test_set_bun_assigns_correct_value(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверяем, что ингредиент добавляется в список
    @patch("praktikum.ingredient.Ingredient")
    def test_add_ingredient_adds_to_list(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    # Проверяем корректное удаление ингредиента
    def test_remove_ingredient_removes_correctly(self):
        mock_ing1 = Mock()
        mock_ing2 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ing1)
        burger.add_ingredient(mock_ing2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_ing2]

    # Проверяем, что ингредиент перемещается на нужную позицию
    @pytest.mark.parametrize(
        'index, new_index, expected_order',
        [
            (0, 1, ["mock_2", "mock_1", "mock_3"]),  # Поменяли местами 0 и 1
            (1, 1, ["mock_1", "mock_2", "mock_3"]),  # Оставили на месте
            (2, 0, ["mock_3", "mock_1", "mock_2"])   # Поменяли местами 2 и 0
        ])
    def test_move_ingredient_moves_correctly(self, index, new_index, expected_order):
        mock_1, mock_2, mock_3 = Mock(name="mock_1"), Mock(name="mock_2"), Mock(name="mock_3")
        burger = Burger()
        burger.ingredients = [mock_1, mock_2, mock_3]

        burger.move_ingredient(index, new_index)

        # Сравниваем порядок имен, а не самих моков
        actual_order = [ing._mock_name for ing in burger.ingredients]
        assert actual_order == expected_order, f"Ожидалось {expected_order}, получено {actual_order}"

    # Проверяем корректный расчет стоимости бургера
    @pytest.mark.parametrize(
        'bun_price, ing1_price, ing2_price, expected_total',
        [
            (100.0, 30.0, 50.0, 280.0),
            (200.0, 70.0, 70.0, 540.0),
            (15.1, 5.2, 5.3, 40.7)
        ])
    def test_get_price_calculates_correctly(self, bun_price, ing1_price, ing2_price, expected_total):
        mock_bun = Mock()
        mock_ingredient1, mock_ingredient2 = Mock(), Mock()
        mock_bun.get_price.return_value = bun_price
        mock_ingredient1.get_price.return_value = ing1_price
        mock_ingredient2.get_price.return_value = ing2_price

        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        total_price = burger.get_price()

        print(f"Ожидалось: {expected_total}, Получено: {total_price}")  # Для дебага
        assert round(total_price, 2) == expected_total, "Цена рассчитана неверно."

    # Проверяем корректность формирования рецепта бургера
    def test_get_receipt_returns_correct_format(self):
        mock_bun, mock_ingredient = Mock(), Mock()
        mock_bun.get_name.return_value = "Булка"
        mock_bun.get_price.return_value = 100.0
        mock_ingredient.get_name.return_value = "Сладкий"
        mock_ingredient.get_type.return_value = "соус"
        mock_ingredient.get_price.return_value = 200.0

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()

        expected_receipt = "(==== Булка ====)\n= соус Сладкий =\n(==== Булка ====)\n\nPrice: 400.0"
        assert receipt == expected_receipt
