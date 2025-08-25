import random
import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
import praktikum.ingredient_types as types
from data_for_tests import constants as const


@pytest.fixture(scope="function")
def new_bun():
    """Фикстура создания булки"""
    return Bun(random.choice(const.bun_names)+" булка", random.uniform(const.min_bun_price, const.max_bun_price))


@pytest.fixture(scope="function")
def new_ingredient():
    """Фикстура создания нового рандомного ингредиента: соуса или начинки"""
    ingredient_type = random.choice([types.INGREDIENT_TYPE_SAUCE, types.INGREDIENT_TYPE_FILLING])
    if ingredient_type == types.INGREDIENT_TYPE_FILLING:
        ingredient_name = random.choice(const.fillings)
        ingredient_price = random.uniform(const.min_filling_price, const.max_filling_price)
    else:
        ingredient_name = random.choice(const.sauces)
        ingredient_price = random.uniform(const.min_sauces_price, const.max_sauces_price)
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_sauce():
    """Фикстура создания соуса"""
    ingredient_type = types.INGREDIENT_TYPE_SAUCE
    ingredient_name = random.choice(const.sauces)
    ingredient_price = random.uniform(const.min_sauces_price, const.max_sauces_price)
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_filling():
    """Фикстура создания начинки"""
    ingredient_type = types.INGREDIENT_TYPE_FILLING
    ingredient_name = random.choice(const.fillings)
    ingredient_price = random.uniform(const.min_filling_price, const.max_filling_price)
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)


@pytest.fixture(scope="function")
def new_burger(new_bun, new_filling, new_sauce):
    """Фикстура создания бургера"""
    burger = Burger()
    burger.set_buns(new_bun)
    burger.add_ingredient(new_filling)
    burger.add_ingredient(new_sauce)
    return burger