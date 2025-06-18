import pytest
from praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture
def empty_burger():
    # Свежесозданный бургер без всего
    return Burger()

@pytest.fixture
def fake_bun():
    # Мок-объект булки с кастомным поведением
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 150.0
    return bun

@pytest.fixture
def fake_ingredient():
    # Мок для любого ингредиента (соус/начинка)
    ingr = Mock()
    ingr.get_type.return_value = "FILLING"
    ingr.get_name.return_value = "pepperoni"
    ingr.get_price.return_value = 75.0
    return ingr

def test_new_burger_has_no_bun(empty_burger):
    # Проверяем, что булочка не назначена при создании
    assert empty_burger.bun is None

def test_new_burger_has_no_ingredients(empty_burger):
    # Новый бургер не содержит начинок
    assert empty_burger.ingredients == []

def test_bun_assignment_works(empty_burger, fake_bun):
    # Можно назначить булочку бургеру
    empty_burger.set_buns(fake_bun)
    assert empty_burger.bun == fake_bun

def test_adding_ingredient_changes_list(empty_burger, fake_ingredient):
    # Добавление ингредиента увеличивает список
    old = len(empty_burger.ingredients)
    empty_burger.add_ingredient(fake_ingredient)
    assert len(empty_burger.ingredients) == old + 1

def test_removing_ingredient_shrinks_list(empty_burger, fake_ingredient):
    # Удаление ингредиента уменьшает длину списка
    empty_burger.add_ingredient(fake_ingredient)
    empty_burger.remove_ingredient(0)
    assert empty_burger.ingredients == []

def test_can_reorder_ingredients(empty_burger):
    # Проверим возможность менять порядок начинок
    first = Mock()
    second = Mock()
    empty_burger.add_ingredient(first)
    empty_burger.add_ingredient(second)
    empty_burger.move_ingredient(0, 1)
    assert empty_burger.ingredients == [second, first]

@pytest.mark.parametrize("bun_price", [100.0, 200.0])
def test_price_counts_buns_twice(empty_burger, fake_bun, bun_price):
    # Стоимость учитывает обе половинки булки
    fake_bun.get_price.return_value = bun_price
    empty_burger.set_buns(fake_bun)
    assert empty_burger.get_price() == bun_price * 2

@pytest.mark.parametrize("bun_price, ingr_price", [(100.0, 50.0), (250.0, 125.0)])
def test_price_with_ingredient(empty_burger, fake_bun, fake_ingredient, bun_price, ingr_price):
    # Цена бургера складывается из двух булок и одной начинки
    fake_bun.get_price.return_value = bun_price
    fake_ingredient.get_price.return_value = ingr_price
    empty_burger.set_buns(fake_bun)
    empty_burger.add_ingredient(fake_ingredient)
    assert empty_burger.get_price() == bun_price * 2 + ingr_price

def test_receipt_content_is_reasonable(empty_burger, fake_bun, fake_ingredient):
    # Чек содержит имена булки и начинки, а также сумму
    fake_bun.get_name.return_value = "parmesan bun"
    fake_bun.get_price.return_value = 100.0
    fake_ingredient.get_type.return_value = "SAUCE"
    fake_ingredient.get_name.return_value = "spicy ketchup"
    fake_ingredient.get_price.return_value = 35.0

    empty_burger.set_buns(fake_bun)
    empty_burger.add_ingredient(fake_ingredient)

    receipt = empty_burger.get_receipt()
    assert "parmesan bun" in receipt
    assert "spicy ketchup" in receipt
    assert str(100.0 * 2 + 35.0) in receipt
