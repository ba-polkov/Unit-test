
from burger import Burger
from unittest.mock import patch
from conftest import *
from data import BurgerGetPrice as bp, BurgerConsist as bc


class TestBurger:

    @allure.title('проверка добавления 1 булки')
    def test_set_buns(self, mock_white_bun):
        burger = Burger()
        burger.set_buns(mock_white_bun)

        assert (burger.bun.name == bc.FIRST_BUN_NAME and burger.bun.price == bc.FIRST_BUN_PRICE
                and burger.bun.name is not None)

    @allure.title('проверка добавление 2 булок')
    def test_set_two_buns(self, mock_white_bun, mock_red_bun):
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.set_buns(mock_red_bun)

        assert (burger.bun.name == bc.SECOND_BUN_NAME and burger.bun.price == bc.SECOND_BUN_PRICE
                and burger.bun.name is not None)


    @allure.title('проверка добавления 1 ингредиента')
    def test_add_one_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)

        assert len(burger.ingredients) == 1

    @allure.title('проверка добавления 2 ингредиентов - соус и начинка')
    def test_add_two_ingredients(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 2


    @allure.title('проверка добавления 2 соусов')
    def test_add_two_sauces(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_sauce)

        assert len(burger.ingredients) == 2


    @allure.title('проверка добавления 2 начинок')
    def test_add_two_fillings(self, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_filling)

        assert len(burger.ingredients) == 2


    @allure.title('проверка удаления 1 ингредиента, если добавлен 1 ингредиент')
    def test_delete_one_ingredient_in_list_with_one_ingredient(self, mock_sauce):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0


    @allure.title('проверка удаления 1 ингредиента, если добавлено 2 ингредиента')
    def test_delete_one_ingredient_in_list_with_two_ingredients(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)  # удаляем ингредиент с индексом 1 или 0

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].type == bc.INGREDIENT_TYPE_FILLING


    # тесты для метода move_ingredient
    @allure.title('проверка на замену местами двух ингредиентов в списке')
    @pytest.mark.parametrize('new_index, old_index', [[0, 1], [1, 0]])
    def test_move_ingredients_in_list(self, mock_sauce, mock_filling, new_index, old_index):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(new_index, old_index)

        assert len(burger.ingredients) == 2
        assert burger.ingredients[0].type == bc.INGREDIENT_TYPE_FILLING
        assert burger.ingredients[1].type == bc.INGREDIENT_TYPE_SAUCE


    @allure.title('получение стоимости бургера с 2 булками и 2 ингредиентами')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_price_with_two_buns_and_sauce_filling(self):
        mock_white_bun = Mock()
        mock_sauce = Mock()
        mock_filling = Mock()
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        mock_sauce.get_price.return_value = bc.SAUCE_PRICE
        mock_filling.get_price.return_value = bc.FILLING_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.get_price() == bp.TWO_BUNS_SAUCE_FILLING_PRICE   # 900 = 900 цена

    @allure.title('получение стоимости бургера с 2 булками')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_price_with_two_buns_and_sauce_filling(self):
        mock_white_bun = Mock()
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)

        assert burger.get_price() == bp.TWO_BUNS_PRICE

    @allure.title('получение стоимости бургера с 2 булками и с соусом')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_price_with_two_buns_and_sauce_filling(self):
        mock_white_bun = Mock()
        mock_sauce = Mock()
        mock_sauce.get_price.return_value = bc.SAUCE_PRICE
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_sauce)

        assert burger.get_price() == bp.BUNS_SAUCE_PRICE

    @allure.title('получение стоимости бургера с 2 булками и ингредиентом')
    @patch('burger.Bun')
    @patch('burger.Ingredient')
    def test_get_price_with_two_buns_and_sauce_filling(self, mock_ingredient_class, mock_bun_class):
        mock_white_bun = Mock()
        mock_filling = Mock()
        mock_filling.get_price.return_value = bc.SAUCE_PRICE
        mock_white_bun.get_price.return_value = bc.FIRST_BUN_PRICE
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_filling)
        print(mock_ingredient_class, mock_bun_class)

        assert burger.get_price() == bp.BUNS_SAUCE_PRICE


    @allure.title('получение рецепта полного бургера')
    def test_get_receipt_full_burger(self, mock_white_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_white_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        mock_white_bun.get_name.return_value = "white bun"
        mock_white_bun.get_price.return_value = 200.0
        mock_sauce.get_type.return_value = 'SAUCE'
        mock_sauce.get_name.return_value = "chili"
        mock_sauce.get_price.return_value = 300.0
        mock_filling.get_type.return_value = 'FILLING'
        mock_filling.get_name.return_value = "dinosaur"
        mock_filling.get_price.return_value = 200.0

        receipt = [
            '(==== white bun ====)',
            '= sauce chili =',
            '= filling dinosaur =',
            '(==== white bun ====)\n',
            'Price: 900.0'
        ]
        assert '\n'.join(receipt) == burger.get_receipt()