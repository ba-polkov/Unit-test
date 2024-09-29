from unittest.mock import Mock

from Diplom_1.data import MockBurger
from Diplom_1.praktikum.bun import Bun
from Diplom_1.praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_bun(self, burger_fixture, bun_fixture):
        bun = burger_fixture

        # Установите макет булочки
        new_bun = Mock(spec=Bun)
        bun.set_buns(new_bun)

        assert bun.bun == new_bun # Проверьте, была ли булочка установлена


    def test_add_ingredient(self, burger_fixture, filling_fixture):
        burger = burger_fixture
        burger.add_ingredient(filling_fixture) # Добавьте ингредиент в бургер

        assert filling_fixture in burger.ingredients # Проверьте, добавился ли ингредиент


    def test_remove_ingredient(self, burger_fixture):
        burger = burger_fixture
        burger.remove_ingredient(0) # Удаляем первый ингредиент
        assert len(burger.ingredients) == 1 and burger.ingredients[0].get_name() == MockBurger.SAUCE_NAME

    def test_move_ingredient(self, burger_fixture, filling_fixture, sauce_fixture):
        burger = burger_fixture
        mock_filling = filling_fixture
        mock_sauce = sauce_fixture

        burger.move_ingredient(0, 1)  # Перемещаем первый ингредиент на вторую позицию

        assert burger.ingredients[0] == mock_sauce and burger.ingredients[1] == mock_filling



    def test_get_price(self, burger_fixture):
        burger = burger_fixture
        price = burger.get_price()

        assert price == 257 * 2 + 424 + 15 # Цена должна быть: 2 * цена булочки + цена соуса + цена начинки

    def test_get_receipt(self, burger_fixture):
        burger = burger_fixture
        expected_receipt = MockBurger.EXPECTED_RECEIPT

        assert burger.get_receipt() == expected_receipt, print(burger.get_receipt())
