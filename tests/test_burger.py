
from praktikum.burger import Burger

class TestBurger:

# Тест установки булки
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

# Тест добавления ингредиента
    def test_add_ingredient(self, mock_ingredient_one):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_one)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient_one

# Тест удаления ингредиента
    def test_remove_ingredient(self, mock_ingredient_one):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_one)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

# Тест перемещения ингредиента
    def test_move_ingredient(self, mock_ingredient_one, mock_ingredient_two):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_two
        assert burger.ingredients[1] == mock_ingredient_one

# Тест расчета цены бургера
    def test_get_price(self, mock_bun, mock_ingredient_one, mock_ingredient_two):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        # Цена булочки (100) * 2 + курица (150) + кетчуп (90) = 440
        assert burger.get_price() == 440


# Тест формирования чека
    def test_get_receipt(self, mock_bun, mock_ingredient_one, mock_ingredient_two):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_one)
        burger.add_ingredient(mock_ingredient_two)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== Булочка ====)\n"
            "= filling Курица =\n"
            "= sauce Кетчуп =\n"
            "(==== Булочка ====)\n"
            "\n"
            "Price: 440"
            )
        assert receipt == expected_receipt