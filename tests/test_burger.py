from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    # Тест установки булки
    def test_set_buns(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Булочка'
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
        assert burger.bun.get_name() == 'Булочка'
        assert burger.bun.get_price() == 100

    # Тест добавления ингредиента
    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_one.get_name.return_value = 'Курица'
        mock_ingredient_one.get_price.return_value = 250
        burger.add_ingredient(mock_ingredient_one)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_one
        assert burger.ingredients[-1].get_name() == 'Курица'
        assert burger.ingredients[-1].get_price() == 250

    # Тест удаления ингредиента
    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_one.get_name.return_value = 'Курица'
        mock_ingredient_one.get_price.return_value = 250
        burger.add_ingredient(mock_ingredient_one)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Тест перемещения ингредиента
    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_one = Mock()
        mock_ingredient_one .get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_one .get_name.return_value = 'Курица'
        mock_ingredient_one .get_price.return_value = 250
        mock_ingredient_two = Mock()
        mock_ingredient_two.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_two.get_name.return_value = 'Кетчуп'
        mock_ingredient_two.get_price.return_value = 90
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_two
        assert burger.ingredients[1] == mock_ingredient_one

    # Тест расчета цены бургера
    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Булочка'
        mock_bun.get_price.return_value = 100
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_one.get_name.return_value = 'Курица'
        mock_ingredient_one.get_price.return_value = 250
        mock_ingredient_two = Mock()
        mock_ingredient_two.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_two.get_name.return_value = 'Кетчуп'
        mock_ingredient_two.get_price.return_value = 90
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        # Цена булочки (100) * 2 + курица (250) + кетчуп (90) = 540
        assert burger.get_price() == 540

    # Тест формирования чека
    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Булочка'
        mock_bun.get_price.return_value = 100
        mock_ingredient_one = Mock()
        mock_ingredient_one.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient_one.get_name.return_value = 'Курица'
        mock_ingredient_one.get_price.return_value = 250
        mock_ingredient_two = Mock()
        mock_ingredient_two.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient_two.get_name.return_value = 'Кетчуп'
        mock_ingredient_two.get_price.return_value = 90
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        receipt = burger.get_receipt()
        expected_receipt = (
            '(==== Булочка ====)\n'
            '= filling Курица =\n'
            '= sauce Кетчуп =\n'
            '(==== Булочка ====)\n'
            '\n'
            'Price: 540'
            )
        assert receipt == expected_receipt

