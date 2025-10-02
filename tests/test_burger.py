import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import TestData


class TestBurger:

    def test_set_buns(self):
        """Тестирование метода выбора булки"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[0][0]
        mock_bun.get_price.return_value = TestData.buns[0][1]
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        """Тестирование метода добавления ингредиента"""
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[9][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[9][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):
        """Тестирование метода удаления ингредиента"""
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[0][2]
        mock_ingredient.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        """Тестирование метода перемещения ингредиента"""
        burger = Burger()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        mock_ingredient3 = Mock()

        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        burger.add_ingredient(mock_ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient3
        assert burger.ingredients[2] == mock_ingredient1

    def test_get_price(self):
        """Тестирование метода получения цены"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = TestData.buns[1][1]

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = TestData.ingredients[1][2]

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = TestData.ingredients[6][2]

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        expected_price = (
            mock_bun.get_price() * 2
            + mock_ingredient1.get_price()
            + mock_ingredient2.get_price()
        )
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        """Тестирование метода получения чека"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[1][0]
        mock_bun.get_price.return_value = TestData.buns[1][1]

        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient1.get_price.return_value = TestData.ingredients[0][2]

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient2.get_name.return_value = TestData.ingredients[6][1]
        mock_ingredient2.get_price.return_value = TestData.ingredients[6][2]

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        receipt = burger.get_receipt()

        assert TestData.buns[1][0] in receipt
        assert TestData.ingredients[0][1] in receipt
        assert TestData.ingredients[6][1] in receipt
        assert "filling" in receipt.lower()
        assert "sauce" in receipt.lower()
        assert "Price:" in receipt

    # Граничные случаи и негативные тесты
    def test_get_price_without_bun_raises_error(self):
        """Тест: получение цены без булки вызывает ошибку"""
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt_without_bun_raises_error(self):
        """Тест: получение чека без булки вызывает ошибку"""
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "Test Ingredient"
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(AttributeError):
            burger.get_receipt()

    def test_remove_ingredient_invalid_index_raises_error(self):
        """Тест: удаление с неверным индексом вызывает ошибку"""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(IndexError):
            burger.remove_ingredient(5)

    def test_move_ingredient_invalid_index_raises_error(self):
        """Тест: перемещение с неверным индексом вызывает ошибку"""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)

    def test_get_price_empty_burger_only_bun(self):
        """Тест: цена бургера только с булкой"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        assert burger.get_price() == 200

    def test_get_receipt_single_ingredient(self):
        """Тест: чек бургера с одним ингредиентом"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Test Bun"
        mock_bun.get_price.return_value = 100

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = "Test Filling"
        mock_ingredient.get_price.return_value = 50

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()
        assert "Test Bun" in receipt
        assert "Test Filling" in receipt
        assert "filling" in receipt.lower()
        assert "Price:" in receipt
