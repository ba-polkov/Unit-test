import pytest
from praktikum.burger import Burger
from unittest.mock import MagicMock

class TestBurger:

    def test_burger_set_buns(self):
        """
        Проверяет установку булок
        """
        burger = Burger()
        bun = MagicMock()
        burger.set_buns(bun)
        assert burger.bun == bun


    def test_burger_add_ingredient(self):
        """
        Проверяет добавление ингредиентов
        """
        burger = Burger()
        ingredient = MagicMock()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]


    def test_burger_remove_ingredient(self):
        """
        Проверяет удаление ингредиентов по индексу
        """
        burger = Burger()
        ingredient1 = MagicMock()
        ingredient2 = MagicMock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient2]


    def test_burger_move_ingredient(self):
        """
        Проверяет перемещение ингредиентов
        """
        burger = Burger()
        ingredient1 = MagicMock()
        ingredient2 = MagicMock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient2, ingredient1]


    @pytest.mark.parametrize("bun_price, ingredient_prices, expected_price", [
        (100, [], 200),
        (100, [50], 250),
        (150, [50, 100], 450),
        (0, [0, 0], 0),
        (99.99, [10.5, 20.75], 231.24)
    ])
    def test_burger_get_price(self, mocker, bun_price, ingredient_prices, expected_price):
        """
        Проверяет расчет цены с разными комбинациями цен
        Использует моки для изоляции от реальных объектов
        """
        mock_bun = mocker.Mock()
        mock_bun.get_price.return_value = bun_price
        burger = Burger()
        burger.set_buns(mock_bun)
        
        for price in ingredient_prices:
            mock_ingredient = mocker.Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == pytest.approx(expected_price, 0.01)


    def test_burger_get_receipt(self, mocker):
        """
        Проверяет форматирование чека
        Использует моки для контроля возвращаемых значений
        """
        mock_bun = mocker.Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100  

        mock_ingredient = mocker.Mock()
        mock_ingredient.get_type.return_value = "SAUCE"
        mock_ingredient.get_name.return_value = "hot sauce"
        mock_ingredient.get_price.return_value = 100  

        burger = Burger()  
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 300"  
        )
        assert burger.get_receipt() == expected