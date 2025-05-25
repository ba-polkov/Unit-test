import allure

from data_for_test import TestIngredientsData as TID, TestBunsData as TBD, TestReceipt as TR
from conftest import mock, create_test_burger, mock_test_bun, mock_test_ingredient
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestClassBurger:
    @allure.title('Значение атрибута "bun"')
    def test_create_burger_bun_is_none(self, create_test_burger):
        assert create_test_burger.bun is None

    @allure.title('Значение атрибута "ingredients"')
    def test_create_burger_ingredients_empty_list(self, create_test_burger):
        assert create_test_burger.ingredients == []

    @allure.title('В "bun" устанавливается объект "Bun"')
    def test_bun_set_valid_attribute(self, mock_test_bun, create_test_burger):
        create_test_burger.set_buns(mock_test_bun)
        assert create_test_burger.bun == mock_test_bun

    @allure.title('В список ингредиентов добавляется объект "Ingredient"')
    def test_added_ingredient_to_burger(self, mock_test_ingredient, create_test_burger):
        create_test_burger.add_ingredient(mock_test_ingredient)
        assert len(create_test_burger.ingredients) > 0

    @allure.title('Перемещение ингредиента бургрера')
    def test_move_ingredient_burger(self, create_test_burger):
        create_test_burger.add_ingredient(TID.INGREDIENTS[0])
        create_test_burger.add_ingredient(TID.INGREDIENTS[3])
        create_test_burger.move_ingredient(0, 1)
        assert (create_test_burger.ingredients[0] == TID.INGREDIENTS[3]
                and create_test_burger.ingredients[1] == TID.INGREDIENTS[0])

    @allure.title('Удаление ингредиента бургера')
    def test_delete_ingredient_to_burger(self, create_test_burger, mock_test_ingredient):
        create_test_burger.add_ingredient(mock_test_ingredient)
        create_test_burger.remove_ingredient(0)
        assert len(create_test_burger.ingredients) == 0

    @allure.title('Получение стоимости бургера')
    def test_get_price_burger(self, create_test_burger):
        create_test_burger.set_buns(Bun(**TBD.BUN))
        create_test_burger.add_ingredient(Ingredient(**TID.INGREDIENT))
        assert create_test_burger.get_price() == 250

    @allure.title('Получение рецепта бургера')
    def test_get_receipt_burger(self, create_test_burger):
        create_test_burger.set_buns(Bun(**TBD.BUN))
        create_test_burger.add_ingredient(Ingredient(**TID.SAUCE))
        create_test_burger.add_ingredient(Ingredient(**TID.FILLING))
        assert create_test_burger.get_receipt() == TR.EXPECTED_RECEIPT