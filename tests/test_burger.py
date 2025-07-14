from unittest.mock import MagicMock
import pytest

class TestBurger:
    def test_set_name_bun(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, ingredient_from_db):
        burger.add_ingredient(ingredient_from_db)
        assert burger.ingredients[0] == ingredient_from_db

    def test_del_ingradient(self, burger, ingredient_from_class, index = 0):
        burger.add_ingredient(ingredient_from_class)
        burger.remove_ingredient(index)
        assert burger.ingredients == []
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, ingredient_mock, ingredient_from_db):
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(ingredient_from_db)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_from_db

    @pytest.mark.parametrize("ingredient_data, result", [
        ([("Напонитель", "Халапеньо", 50.0), ("Соусо", "Горчичный", 20.0)], 470.0),
        ([("Напонитель", "Грибы", 10.0), ("Соус", "Чесночный", 15.0)], 425.0)])
    def test_get_price(self, burger, bun, ingredient_data, result):
        burger.set_buns(bun)
        for ingredient_type, name, price in ingredient_data:
            ingredient_mock = MagicMock()
            ingredient_mock.get_type.return_value = ingredient_type
            ingredient_mock.get_name.return_value = name
            ingredient_mock.get_price.return_value = price
            burger.add_ingredient(ingredient_mock)
        assert result == burger.get_price()

    def test_get_receipt(self, burger, bun, ingredient_from_db):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_from_db)
        result = f'(==== {bun.get_name()} ====)\n'\
                           f'= {ingredient_from_db.get_type().lower()} {ingredient_from_db.get_name()} =\n'\
                           f'(==== {bun.get_name()} ====)\n'\
                           '\n'\
                           f'Price: {burger.get_price()}'
        assert burger.get_receipt() == result
