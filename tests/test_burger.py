from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_ctor(self, burger):
        assert not burger.bun and len(burger.ingredients) == 0

    def test_set_buns(self, burger):
        bun = Bun('Глю', 5.25)
        burger.set_buns(bun)
        assert bun == burger.bun

    def test_add_ingredient(self, burger_ready):
        ingredient_to_add = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Бама', 0.05)
        burger_ready.add_ingredient(ingredient_to_add)
        assert ingredient_to_add == burger_ready.ingredients[-1]

    def test_remove_ingredient(self, burger_ready):
        ingredient_index = 1
        ingredient_to_remove = burger_ready.ingredients[ingredient_index]
        burger_ready.remove_ingredient(ingredient_index)
        assert ingredient_to_remove not in burger_ready.ingredients

    def test_move_ingredient(self, burger_ready):
        ingredient_old_index = 2
        ingredient_new_index = 0
        ingredient_to_move = burger_ready.ingredients[ingredient_old_index]
        burger_ready.move_ingredient(ingredient_old_index, ingredient_new_index)
        assert ingredient_to_move == burger_ready.ingredients[ingredient_new_index] \
            and ingredient_to_move != burger_ready.ingredients[ingredient_old_index]
    
    def test_get_price(self, burger_ready):
        assert 15.99 == burger_ready.get_price()

    def test_get_receipt(self, burger_ready):
        assert burger_ready.get_receipt() == \
              '(==== Корж ржаной ====)\n' \
            + '= sauce Кетчуп Джой =\n' \
            + '= filling Лук Порей =\n' \
            + '= filling Рыба Лупо =\n' \
            + '= filling Томат Ост =\n' \
            + '= filling Салат Айс =\n' \
            + '(==== Корж ржаной ====)\n' \
            + '\n' \
            + 'Price: 15.99'
