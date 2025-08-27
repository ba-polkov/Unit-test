import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


class TestBurger:

    def test_ctor(self, burger):
        assert not burger.bun and len(burger.ingredients) == 0

    def test_set_buns(self, burger):
        bun = Bun('Глю', 5.25)
        burger.set_buns(bun)
        assert bun == burger.bun

    def test_add_ingredient(self, burger_ready):
        ingredient_to_add = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Бама', 0.05)
        count = len(burger_ready.ingredients)
        burger_ready.add_ingredient(ingredient_to_add)
        assert ingredient_to_add == burger_ready.ingredients[-1] \
            and count + 1 == len(burger_ready.ingredients)

    @pytest.mark.parametrize('index', [2, 0, 4])  # из середины, начала, конца
    def test_remove_ingredient(self, burger_ready, index):
        index = 1
        ingredient_to_remove = burger_ready.ingredients[index]
        count = len(burger_ready.ingredients)
        burger_ready.remove_ingredient(index)
        assert ingredient_to_remove not in burger_ready.ingredients \
            and count - 1 == len(burger_ready.ingredients)

    @pytest.mark.parametrize('old_index, new_index',
        [
            (1,2), (2,1),  # соседние из середины 
            (0,2), (2,0),  # голова - середина
            (0,4), (4,0),  # голова - хвост
            (2,4), (4,2),  # хвост - середина
        ])
    def test_move_ingredient(self, burger_ready, old_index, new_index):
        ingredient_to_move = burger_ready.ingredients[old_index]
        count = len(burger_ready.ingredients)
        burger_ready.move_ingredient(old_index, new_index)
        assert ingredient_to_move == burger_ready.ingredients[new_index] \
            and ingredient_to_move != burger_ready.ingredients[old_index] \
            and count == len(burger_ready.ingredients)
    
    def test_get_price_for_empty_burger(self, burger):
        with pytest.raises(Exception): 
            burger.get_price()

    def test_get_price(self, burger_ready):
        assert 15.99 == burger_ready.get_price()

    # Если представить, что Bun и Ingredient объекты, которые очень сложно  
    # создать или ввести в нужное состояние, то их следует мокать
    # как в тесте ниже
    def test_get_price_mock_version(self):
        bun_mock = Mock()
        bun_mock.get_price.return_value = 10.05
        ingredient_mock = Mock()
        ingredient_mock.get_price.return_value = 4.02
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert 24.12 == burger.get_price()

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
