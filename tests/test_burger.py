from praktikum.burger import Burger
import allure
from data import Data


class TestBurger:
	@allure.title('Проверка инициализации bun и ingredients')
	def test_init(self):
		burger = Burger()
		assert burger.bun is None and burger.ingredients == []

	@allure.title('Проверка метода set_buns')
	def test_set_buns(self, mock_bun):
		burger = Burger()
		burger.set_buns(mock_bun)
		assert burger.bun == mock_bun

	@allure.title('Проверка метода add_ingredient')
	def test_add_ingredient(self, mock_filling):
		burger = Burger()
		burger.add_ingredient(mock_filling)
		assert mock_filling in burger.ingredients

	@allure.title('Проверка метода remove_ingredient')
	def test_remove_ingredient(self, mock_filling):
		burger = Burger()
		burger.add_ingredient(mock_filling)
		burger.remove_ingredient(0)
		assert mock_filling not in burger.ingredients

	@allure.title('Проверка метода move_ingredient')
	def test_move_ingredient(self, mock_filling, mock_sauce):
		burger = Burger()
		burger.add_ingredient(mock_filling)
		burger.add_ingredient(mock_sauce)
		burger.move_ingredient(1, 0)
		assert burger.ingredients[0] == mock_sauce

	@allure.title('Проверка метода get_price')
	def test_get_price_ingredient(self, mock_bun, mock_filling, mock_sauce):
		burger = Burger()
		burger.set_buns(mock_bun)
		burger.add_ingredient(mock_filling)
		burger.add_ingredient(mock_sauce)
		assert burger.get_price() == Data.burger_sum_price

	@allure.title('Проверка метода get_receipt')
	def test_get_receipt_success(self, mock_bun, mock_sauce, mock_filling):
		burger = Burger()
		burger.set_buns(mock_bun)
		burger.add_ingredient(mock_sauce)
		burger.add_ingredient(mock_filling)
		assert burger.get_receipt() == ('(==== white bun ====)\n'
										'= sauce hot sauce =\n'
										'= filling cutlet =\n'
										'(==== white bun ====)\n'
										'\n'
										f'Price: {burger.get_price()}')