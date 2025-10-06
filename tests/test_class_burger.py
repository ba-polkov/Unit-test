import pytest

from unittest.mock import Mock
from data import BurgerElements as BE, IngredientIndex as II, BurgerPrices as BP
from burger import Burger


# Тесты, покрывающие класс Burger
class TestBurgerClass:

    # Тесты для конструктора __init__
    # Проверяем, что при при создании объекта класса Burger в нём нет булок
    def test_new_burger_no_buns_true(self):
        burger = Burger()
        assert burger.bun == None

    # Проверяем, что при создании объекта класса Burger в нём нет ингредиентов
    def test_new_burger_no_ingredients_true(self):
        burger = Burger()
        assert burger.ingredients == []

    # Тесты для метода set_buns()
    # Добавление любой булки из набора булок в бургер (3 варианта)
    @pytest.mark.parametrize('bun_name, bun_price',
                             [
                                 (BE.BUN_NAME_1, BE.BUN_PRICE_1),
                                 (BE.BUN_NAME_2, BE.BUN_PRICE_2),
                                 (BE.BUN_NAME_3, BE.BUN_PRICE_3)
                             ]
                             )
    def test_set_buns_1_bun_successfully(self, bun_name, bun_price):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.name = bun_name
        mock_bun.price = bun_price
        burger.set_buns(mock_bun)
        assert burger.bun.name == bun_name and burger.bun.price == bun_price

    # Добавление верхней и нижней булок в бургер
    def test_set_buns_upper_and_lower_buns_successfully(self):
        burger = Burger()
        mock_bun_1 = Mock()
        mock_bun_1.name = BE.BUN_NAME_1
        mock_bun_1.price = BE.BUN_PRICE_1
        mock_bun_2 = Mock()
        mock_bun_2.name = BE.BUN_NAME_2
        mock_bun_2.price = BE.BUN_PRICE_2
        burger.set_buns(mock_bun_1)
        burger.set_buns(mock_bun_2)
        assert burger.bun.name == BE.BUN_NAME_2 and burger.bun.price == BE.BUN_PRICE_2

    # Тесты для метода add_ingredient()
    # Добавление любого ингредиента из набора в бургер (6 вариантов)
    @pytest.mark.parametrize('ingredient_type, ingredient_name, ingredient_price',
                             [
                                 (BE.INGREDIENT_TYPE_1, BE.SAUCE_NAME_1, BE.SAUCE_PRICE_1),
                                 (BE.INGREDIENT_TYPE_1, BE.SAUCE_NAME_2, BE.SAUCE_PRICE_2),
                                 (BE.INGREDIENT_TYPE_1, BE.SAUCE_NAME_3, BE.SAUCE_PRICE_3),
                                 (BE.INGREDIENT_TYPE_2, BE.FILLING_NAME_1, BE.FILLING_PRICE_1),
                                 (BE.INGREDIENT_TYPE_2, BE.FILLING_NAME_2, BE.FILLING_PRICE_2),
                                 (BE.INGREDIENT_TYPE_2, BE.FILLING_NAME_3, BE.FILLING_PRICE_3)
                            ]
                             )
    def test_add_ingredient_any_ingredient_successfully(self, ingredient_type, ingredient_name, ingredient_price):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.ingredient_type = ingredient_type
        mock_ingredient.name = ingredient_name
        mock_ingredient.price = ingredient_price
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    # Добавление 1 соуса и 1 начинки из набора в бургер
    def test_add_ingredient_1_sauce_and_1_filling(self, mock_sauce_1, mock_filling_1):
        burger = Burger()
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        assert len(burger.ingredients) == 2 and burger.ingredients[0].name == BE.SAUCE_NAME_1 and burger.ingredients[1].name == BE.FILLING_NAME_1

    # Добавление 2 разных соусов и 2 разных начинок из набора в бургер
    def test_add_ingredient_2_sauces_and_2_fillings(self, mock_sauce_2, mock_sauce_3, mock_filling_2, mock_filling_3):
        burger = Burger()
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_sauce_3)
        burger.add_ingredient(mock_filling_2)
        burger.add_ingredient(mock_filling_3)
        assert len(burger.ingredients) == 4 and burger.ingredients[1].name == BE.SAUCE_NAME_3 and burger.ingredients[3].name == BE.FILLING_NAME_3

    # Добавление 3 одинаковых соусов и 3 одинаковых начинок из ассортимента в бургер
    def test_add_ingredients_3_same_sauces_and_3_same_fillings(self, mock_sauce_1, mock_filling_1):
        burger = Burger()
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        burger.add_ingredient(mock_filling_1)
        burger.add_ingredient(mock_filling_1)
        assert len(burger.ingredients) == 6 and burger.ingredients[1].name == BE.SAUCE_NAME_1 and burger.ingredients[4].name == BE.FILLING_NAME_1

    # Тесты для метода remove_ingredient()
    # Удаляем единственный игредиент из списка
    def test_remove_ingredient_only_one_ingredient_in_list(self, mock_sauce_1):
        burger = Burger()
        burger.add_ingredient(mock_sauce_1)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Удаляем два ингредиента из списка из двух ингредиентов
    def test_remove_ingredient_remove_2_ingredients_from_list(self, mock_sauce_3, mock_filling_3):
        burger = Burger()
        burger.add_ingredient(mock_sauce_3)
        burger.add_ingredient(mock_filling_3)
        burger.remove_ingredient(0)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Удаляем второй ингредиент из списка из двух ингредиентов
    def test_remove_ingredient_remove_second_ingredient_from_list(self, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1 and burger.ingredients[0].name == BE.SAUCE_NAME_2

    # Тесты для метода move_ingredient()
    # Переместить 2 ингредиента в списке и поменять их местами
    def test_move_ingredient_change_2_ingredients(self, mock_sauce_2, mock_filling_2):
        burger = Burger()
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        burger.move_ingredient(II.FIRST_INGREDIENT, II.SECOND_INGREDIENT)
        assert len(burger.ingredients) == 2 and burger.ingredients[0].name == BE.FILLING_NAME_2 and burger.ingredients[1].name == BE.SAUCE_NAME_2

    # Переместить 2 ингредиента на другие места в списке из 3 ингредиентов
    def test_move_ingredient_change_3_ingredients(self, mock_sauce_2, mock_filling_2, mock_sauce_3):
        burger = Burger()
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        burger.add_ingredient(mock_sauce_3)
        burger.move_ingredient(II.FIRST_INGREDIENT, II.THIRD_INGREDIENT)
        burger.move_ingredient(II.SECOND_INGREDIENT, II.THIRD_INGREDIENT)
        assert (len(burger.ingredients) == 3 and
                burger.ingredients[0].name == BE.FILLING_NAME_2 and
                burger.ingredients[1].name == BE.SAUCE_NAME_2 and
                burger.ingredients[2].name == BE.SAUCE_NAME_3)

    # Тесты для метода get_price()
    # Проверяем стоимость бургера с 2 красными булочками, без ингредиентов
    def test_get_price_only_red_buns(self, mock_red_bun):
        burger = Burger()
        burger.set_buns(mock_red_bun)
        assert burger.get_price() == BP.BURGER_PRICE_RED_BUNS

    # Проверяем стоимость бургера с 2 красными булочками, чили соусом и сосиской
    def test_get_price_2_red_buns_and_chili_sauce_and_sausage(self, mock_red_bun, mock_sauce_3, mock_filling_3):
        burger = Burger()
        burger.set_buns(mock_red_bun)
        burger.add_ingredient(mock_sauce_3)
        burger.add_ingredient(mock_filling_3)
        assert burger.get_price() == BP.BURGER_PRICE_RB_CS_S

    # Проверяем стоимость бургера с 2 красными булочками, острым соусом, сметаной, динозавром и сосиской
    def test_get_price_2_red_buns_and_hot_sauce_and_sour_cream_and_dinosaur_and_sausage(self, mock_red_bun, mock_sauce_1, mock_sauce_2, mock_filling_2, mock_filling_3):
        burger = Burger()
        burger.set_buns(mock_red_bun)
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_sauce_2)
        burger.add_ingredient(mock_filling_2)
        burger.add_ingredient(mock_filling_3)
        assert burger.get_price() == BP.BURGER_PRICE_RB_HS_SC_D_S

    # Тесты для метода get_receipt()
    # Проверяем получение рецепта: 2 красные булки
    def test_get_receipt_2_red_buns(self, mock_red_bun):
        burger = Burger()
        burger.set_buns(mock_red_bun)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== red bun ====)\n"
            "(==== red bun ====)\n"
            "\nPrice: 600.0"
        )
        assert len(receipt) > 0 and burger.get_receipt() == expected_receipt

    # Проверяем получение рецепта: 2 красные булки, острый соус и котлета
    def test_get_receipt_2_red_buns_and_hot_sauce_and_cutlet(self, mock_red_bun, mock_sauce_1, mock_filling_1):
        burger = Burger()
        burger.set_buns(mock_red_bun)
        burger.add_ingredient(mock_sauce_1)
        burger.add_ingredient(mock_filling_1)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== red bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== red bun ====)\n"
            "\nPrice: 800.0"
        )
        assert len(receipt) > 0 and burger.get_receipt() == expected_receipt
