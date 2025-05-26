import allure

from data_for_test import TestIngredientsData as TID, TestBunsData as TBD, TestReceipt as TR
from conftest import mock_test_bun, mock_test_ingredient
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

class TestClassBurger:
    @allure.title('Значение атрибута "bun"')
    def test_create_burger_bun_is_none(self):
        assert Burger().bun is None

    @allure.title('Значение атрибута "ingredients"')
    def test_create_burger_ingredients_empty_list(self):
        assert Burger().ingredients == []

    @allure.title('В "bun" устанавливается объект "Bun"')
    def test_bun_set_valid_attribute(self, mock_test_bun):
        burger = Burger()
        burger.set_buns(mock_test_bun)
        assert burger.bun == mock_test_bun

    @allure.title('В список ингредиентов добавляется объект "Ingredient"')
    def test_added_ingredient_to_burger(self, mock_test_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_test_ingredient)
        assert len(burger.ingredients) > 0

    @allure.title('Перемещение ингредиента бургрера')
    def test_move_ingredient_burger(self):
        burger = Burger()
        burger.add_ingredient(TID.INGREDIENTS[0])
        burger.add_ingredient(TID.INGREDIENTS[3])
        burger.move_ingredient(0, 1)
        assert (burger.ingredients[0] == TID.INGREDIENTS[3]
                and burger.ingredients[1] == TID.INGREDIENTS[0])

    @allure.title('Удаление ингредиента бургера')
    def test_delete_ingredient_to_burger(self, mock_test_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_test_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    @allure.title('Получение стоимости бургера')
    def test_get_price_burger(self):
        burger = Burger()
        burger.set_buns(Bun(**TBD.BUN))
        burger.add_ingredient(Ingredient(**TID.INGREDIENT))
        assert burger.get_price() == 250

    @allure.title('Получение рецепта бургера')
    def test_get_receipt_burger(self):
        burger = Burger()
        burger.set_buns(Bun(**TBD.BUN))
        burger.add_ingredient(Ingredient(**TID.SAUCE))
        burger.add_ingredient(Ingredient(**TID.FILLING))
        assert burger.get_receipt() == TR.EXPECTED_RECEIPT