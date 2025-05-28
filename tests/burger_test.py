from data import const
from helpers import TestTools
from praktikum.bun import Bun
from praktikum.burger import Burger

class TestBurger:

    def test_burger_set_buns_make_buns(self):
        burger = Burger()
        burger.set_buns(bun=Bun(name=const['TESTS_DATA_BUN'][0], price=const['TESTS_DATA_BUN'][1]))
        buns = burger.bun.get_name(), burger.bun.get_price()
        TestTools.check_unit_test_result(expected_value=const['TESTS_DATA_BUN'], actually_value=buns)

