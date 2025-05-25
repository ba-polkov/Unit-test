import pytest
from unittest.mock import MagicMock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    # Тесты для класса Burger

    def setup_method(self):
        # Создаю новый объект бургера перед каждым тестом
        self.burger = Burger()

    def test_initialization(self):
        # Проверяю, что бургер инициализируется без булочки и ингредиентов
        assert self.burger.bun is None
        assert len(self.burger.ingredients) == 0

    def test_set_buns(self, mock_bun):
        # Проверяю установку булочки в бургер
        self.burger.set_buns(mock_bun)
        assert self.burger.bun == mock_bun

    def test_add_ingredient(self, mock_sauce, mock_filling):
        # Проверяю добавление ингредиентов (соус и начинка)
        self.burger.add_ingredient(mock_sauce)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == mock_sauce

        self.burger.add_ingredient(mock_filling)
        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[1] == mock_filling

    def test_remove_ingredient(self, mock_sauce, mock_filling):
        # Проверяю удаление ингредиента по индексу
        self.burger.add_ingredient(mock_sauce)
        self.burger.add_ingredient(mock_filling)
        assert len(self.burger.ingredients) == 2

        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == mock_filling

    def test_move_ingredient(self, mock_sauce, mock_filling):
        # Проверяю перемещение ингредиента внутри списка
        self.burger.add_ingredient(mock_sauce)
        self.burger.add_ingredient(mock_filling)

        # Перемещаю соус с позиции 0 на позицию 1
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[0] == mock_filling
        assert self.burger.ingredients[1] == mock_sauce

    def test_get_price(self, mock_bun, mock_sauce, mock_filling):
        # Проверяю правильность расчёта цены бургера
        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_sauce)
        self.burger.add_ingredient(mock_filling)

        # Ожидаемая цена: (цена булочки * 2) + цена соуса + цена начинки
        expected_price = (mock_bun.get_price() * 2) + mock_sauce.get_price() + mock_filling.get_price()
        assert self.burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        # Проверяю правильность формирования чека бургера
        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_sauce)
        self.burger.add_ingredient(mock_filling)

        receipt = self.burger.get_receipt()

        # Проверяю, что чек содержит корректные строки
        assert f"(==== {mock_bun.get_name()} ====)" in receipt
        assert f"= {mock_sauce.get_type().lower()} {mock_sauce.get_name()} =" in receipt
        assert f"= {mock_filling.get_type().lower()} {mock_filling.get_name()} =" in receipt

        # Проверяю, что итоговая цена отображается правильно
        assert f"Price: {self.burger.get_price()}" in receipt

    @patch('praktikum.burger.Burger.get_price')
    def test_get_receipt_with_patched_price(self, mock_get_price, mock_bun, mock_sauce):
        # Проверяю, что при патче цены чек выводит патченный результат
        mock_get_price.return_value = 999

        self.burger.set_buns(mock_bun)
        self.burger.add_ingredient(mock_sauce)

        receipt = self.burger.get_receipt()

        # Проверяю, что чек содержит патченный цену
        assert "Price: 999" in receipt
        mock_get_price.assert_called_once()
