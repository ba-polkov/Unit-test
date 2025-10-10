from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import Data1, Data2
import pytest
import allure


class TestBurger:

    @allure.title('Проверка работы метода set_buns')
    @allure.description('Проверка метода добавляющего булочку')
    def test_set_buns(self):
        bun = Bun(Data1.bun_name, Data1.bun_price)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    @allure.title('Проверка работы метода add_ingredient')
    @allure.description('Проверка добавления соуса и начинок')
    @pytest.mark.parametrize('data_class', [Data1, Data2])
    def test_add_ingredient(self, data_class):
        sauce = Ingredient(data_class.sauce_type, data_class.sauce_name, data_class.sauce_price)
        filling = Ingredient(data_class.filling_type, data_class.filling_name, data_class.filling_price)
        burger = Burger()
        burger.add_ingredient(sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == data_class.sauce_name

        burger.add_ingredient(filling)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[1].get_name() == data_class.filling_name

    @allure.title('Проверка работы метода remove_ingredient')
    @allure.description('Проверка удаления ингредиента по индексу')
    def test_remove_ingredient(self):
        bun = Bun(Data1.bun_name, Data1.bun_price)
        sauce = Ingredient(Data1.sauce_type, Data1.sauce_name, Data1.sauce_price)
        filling = Ingredient(Data1.filling_type, Data1.filling_name, Data1.filling_price)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0].get_name() == Data1.filling_name

    @allure.title('Проверка работы метода move_ingredient')
    @allure.description('Проверка перемещения ингредиентов')
    def test_move_ingredient(self):
        sauce = Ingredient(Data1.sauce_type, Data1.sauce_name, Data1.sauce_price)
        filling = Ingredient(Data1.filling_type, Data1.filling_name, Data1.filling_price)

        burger = Burger()
        burger.add_ingredient(sauce)      # [sauce]
        burger.add_ingredient(filling)    # [sauce, filling]

        # Меняем местами: sauce (0) ↔ filling (1)
        burger.move_ingredient(0, 1)

        assert burger.ingredients[0].get_name() == Data1.filling_name
        assert burger.ingredients[1].get_name() == Data1.sauce_name

    @allure.title('Проверка работы метода get_price')
    @allure.description('Проверка расчёта итоговой стоимости бургера')
    @pytest.mark.parametrize('data_class', [Data1, Data2])
    def test_get_price_burger(self, data_class):
        bun = Bun(data_class.bun_name, data_class.bun_price)
        sauce = Ingredient(data_class.sauce_type, data_class.sauce_name, data_class.sauce_price)
        filling = Ingredient(data_class.filling_type, data_class.filling_name, data_class.filling_price)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        expected_price = data_class.bun_price * 2 + data_class.sauce_price + data_class.filling_price
        assert burger.get_price() == expected_price

    @allure.title('Проверка работы метода get_receipt')
    @allure.description('Проверка формирования рецепта бургера')
    @pytest.mark.parametrize('data_class', [Data1, Data2])
    def test_get_receipt(self, data_class):
        bun = Bun(data_class.bun_name, data_class.bun_price)
        sauce = Ingredient(data_class.sauce_type, data_class.sauce_name, data_class.sauce_price)
        filling = Ingredient(data_class.filling_type, data_class.filling_name, data_class.filling_price)
        filling2= Ingredient(data_class.filling_type, data_class.filling_name, data_class.filling_price)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.add_ingredient(filling2)

        expected_receipt = (f"(==== {data_class.bun_name} ====)\n"
                            f"= sauce {data_class.sauce_name} =\n"
                            f"= filling {data_class.filling_name} =\n"
                            f"= filling {data_class.filling_name} =\n"
                            f"(==== {data_class.bun_name} ====)\n"
                            f"\n"
                            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_receipt