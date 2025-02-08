import pytest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import BunData, IngredientSauceData, IngredientFillingData


@pytest.fixture (scope='function')
def default_bun():
    bun = Bun(BunData.bun_name, BunData.bun_price)
    return bun

@pytest.fixture (scope='function')
def ingredient_sauce():
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE, IngredientSauceData.sauce_name, IngredientSauceData.sauce_price)
    return sauce

@pytest.fixture (scope='function')
def ingredient_filling():
    filling = Ingredient(INGREDIENT_TYPE_FILLING, IngredientFillingData.filling_name, IngredientFillingData.filling_price)
    return filling

