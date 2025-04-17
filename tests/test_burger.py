import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    """Фикстура для создания пустого бургера."""
    return Burger()


@pytest.fixture
def bun():
    """Фикстура для создания булочки."""
    return Bun("black bun", 100)


@pytest.fixture
def ingredient_sauce():
    """Фикстура для создания соуса."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)


@pytest.fixture
def ingredient_filling():
    """Фикстура для создания начинки."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)


def test_set_buns(burger, bun):
    """Тест на установку булочки для бургера."""
    burger.set_buns(bun)
    assert burger.bun.get_name() == "black bun"
    assert burger.bun.get_price() == 100


def test_add_ingredient(burger, ingredient_sauce):
    """Тест на добавление ингредиента в бургер."""
    burger.add_ingredient(ingredient_sauce)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0].get_name() == "hot sauce"
    assert burger.ingredients[0].get_price() == 50


def test_remove_ingredient(burger, ingredient_sauce):
    """Тест на удаление ингредиента из бургера."""
    burger.add_ingredient(ingredient_sauce)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 0


def test_move_ingredient(burger, ingredient_sauce, ingredient_filling):
    """Тест на перемещение ингредиента в бургер."""
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    burger.move_ingredient(1, 0)
    assert burger.ingredients[0].get_name() == "cutlet"
    assert burger.ingredients[1].get_name() == "hot sauce"


def test_get_price(burger, bun, ingredient_sauce, ingredient_filling):
    """Тест на расчет цены бургера."""
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    assert burger.get_price() == 400  # 2 * 100 (булочка) + 50 (соус) + 150 (начинка)


def test_get_receipt(burger, bun, ingredient_sauce, ingredient_filling):
    """Тест на генерацию чека для бургера."""
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    receipt = burger.get_receipt()
    assert "Price: 400" in receipt
    assert "(==== black bun ====)" in receipt
    assert "= sauce hot sauce =" in receipt
    assert "= filling cutlet =" in receipt