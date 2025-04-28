import allure
import pytest
from conftest import *
from praktikum.burger import Burger
from data import Data

class TestBurger:

    @allure.title('Проверка метода set_buns ')
    def test_set_buns(self,burger_fixture, mock_bun):
        assert burger_fixture.bun == mock_bun
        assert burger_fixture.bun.get_name() == Data.Bun_name

    @allure.title('Проверка метода add_ingredient через параметризацию, путем добавления начинок')
    @pytest.mark.parametrize('ingredient_name, ingridient_added_name',
                             [
                             [Data.Sauce_name, Data.Sauce_name],
                             [Data.Filling_name, Data.Filling_name]
                             ])
    def test_add_ingredient(self,burger_fixture, ingredient_name, ingridient_added_name):
        bf = burger_fixture.add_ingredient(ingredient_name)
        assert bf == [ingridient_added_name]
