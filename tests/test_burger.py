import pytest
from unittest.mock import MagicMock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns(self,empty_burger, default_bun):
        empty_burger.set_buns(default_bun)
        assert empty_burger.bun == default_bun, "Булочка не была установлена корректно"

    def test_add_ingredient(self,empty_burger, ingredient_sauce):
        empty_burger.add_ingredient(ingredient_sauce)
        assert ingredient_sauce in empty_burger.ingredients, "Ингредиент не был добавлен в бургер"

    def test_remove_ingredient(self,prepared_burger):
        initial_length = len(prepared_burger.ingredients)
        prepared_burger.remove_ingredient(0)
        assert len(prepared_burger.ingredients) == initial_length - 1, "Ингредиент не был удален из бургера"

    def test_move_ingredient(self,prepared_burger):
        first_ingredient = prepared_burger.ingredients[0]
        second_ingredient = prepared_burger.ingredients[1]
        prepared_burger.move_ingredient(0, 1)
        assert prepared_burger.ingredients[1] == first_ingredient, "Ингредиент не был перемещен корректно"
        assert prepared_burger.ingredients[0] == second_ingredient, "Ингредиенты не поменялись местами"

    def test_get_price(self,prepared_burger):
        expected_price = prepared_burger.bun.get_price() * 2
        for ingredient in prepared_burger.ingredients:
            expected_price += ingredient.get_price()
        assert prepared_burger.get_price() == expected_price, "Цена бургера рассчитана некорректно"

    def test_get_receipt(self,prepared_burger):
        receipt = prepared_burger.get_receipt()
        assert isinstance(receipt, str), "Чек должен быть строкой"
        assert prepared_burger.bun.get_name() in receipt, "Название булочки должно присутствовать в чеке"
        for ingredient in prepared_burger.ingredients:
            assert ingredient.get_name() in receipt, f"Ингредиент {ingredient.get_name()} должен присутствовать в чеке"
            assert str(prepared_burger.get_price()) in receipt, "Цена бургера должна присутствовать в чеке"

    @pytest.mark.parametrize("ingredient_type", ["SAUCE", "FILLING"])
    def test_add_multiple_ingredients(self,empty_burger, ingredient_type):
        ingredient = Ingredient(f"Тестовый ингредиент {ingredient_type}", 1.0, ingredient_type)
        empty_burger.add_ingredient(ingredient)
        assert empty_burger.ingredients[0] == ingredient, "Ингредиент не был добавлен в бургер"

    def test_get_price_with_mocked_bun_and_ingredients(self,empty_burger):
        mock_bun = MagicMock(spec=Bun)
        mock_bun.get_price.return_value = 1.5
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 0.75
        empty_burger.set_buns(mock_bun)
        empty_burger.add_ingredient(mock_ingredient)
        empty_burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price() * 2
        assert empty_burger.get_price() == expected_price, "Цена бургера с моками рассчитана некорректно"

    def test_get_receipt_with_mocked_methods(self,prepared_burger):
        with patch.object(Bun, 'get_name', return_value="Моковая булочка") as mock_bun_name:
            with patch.object(Ingredient, 'get_name',
                              side_effect=["Моковый соус", "Моковая начинка"]) as mock_ingredient_name:
                with patch.object(Ingredient, 'get_type', side_effect=["SAUCE", "FILLING"]) as mock_ingredient_type:
                    receipt = prepared_burger.get_receipt()
                    assert "Моковая булочка" in receipt, "Название моковой булочки должно присутствовать в чеке"
                    assert "Моковый соус" in receipt, "Название мокового соуса должно присутствовать в чеке"
                    assert "Моковая начинка" in receipt, "Название моковой начинки должно присутствовать в чеке"
