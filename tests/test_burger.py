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
    @pytest.mark.parametrize('ingredient_name, expected_ingredient_added_name',
                             [
                                 ('mock_sauce', Data.Sauce_name),
                                 ('mock_filling', Data.Filling_name)
                             ])
    def test_add_ingredient(self,burger_fixture, request, ingredient_name, expected_ingredient_added_name):
        ingredient = request.getfixturevalue(ingredient_name)
        bf = burger_fixture
        bf.add_ingredient(ingredient)
        assert bf.ingredients[0].get_name() == expected_ingredient_added_name

    @allure.title('роверка метода remove_ingredient через параметризацию, путем добавления и удаления начинок')
    @pytest.mark.parametrize('ingredient_name, expected_ingridient_removed_name',
                             [
                                 ('mock_sauce', Data.Sauce_name),
                                 ('mock_filling', Data.Filling_name)
                             ])
    def test_remove_ingredient(self, burger_fixture, request, ingredient_name, expected_ingridient_removed_name):
        ingredient = request.getfixturevalue(ingredient_name)
        bf = burger_fixture
        bf.add_ingredient(ingredient)
        assert ingredient in bf.ingredients
        index = bf.ingredients.index(ingredient)
        bf.remove_ingredient(index)
        assert expected_ingridient_removed_name not in [ing.get_name() for ing in bf.ingredients]