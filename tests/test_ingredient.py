import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Набор тестовых ингредиентов для проверки разных сценариев
ingredient_cases = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300.0),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0),
    (INGREDIENT_TYPE_FILLING, "sausage", 300.0),
]

@pytest.mark.parametrize("type_, name, price", ingredient_cases)
def test_ingredient_type_is_saved(type_, name, price):
    # Проверяем, что тип ингредиента сохраняется корректно
    ingr = Ingredient(type_, name, price)
    assert ingr.type == type_

@pytest.mark.parametrize("type_, name, price", ingredient_cases)
def test_ingredient_name_is_saved(type_, name, price):
    # Проверяем, что название ингредиента записывается верно
    ingr = Ingredient(type_, name, price)
    assert ingr.name == name

@pytest.mark.parametrize("type_, name, price", ingredient_cases)
def test_ingredient_price_is_saved(type_, name, price):
    # Удостоверяемся, что цена ингредиента не искажается
    ingr = Ingredient(type_, name, price)
    assert ingr.price == price

@pytest.mark.parametrize("type_, name, price", ingredient_cases)
def test_get_type_returns_real_type(type_, name, price):
    # Геттер возвращает тот же тип, что был задан
    ingr = Ingredient(type_, name, price)
    assert ingr.get_type() == type_

@pytest.mark.parametrize("type_, name, price", ingredient_cases)
def test_get_name_returns_real_name(type_, name, price):
    # Геттер возвращает имя, которое мы задали
    ingr = Ingredient(type_, name, price)
    assert ingr.get_name() == name

@pytest.mark.parametrize("type_, name, price", ingredient_cases)
def test_get_price_returns_real_price(type_, name, price):
    # Проверка правильности возврата стоимости ингредиента
    ingr = Ingredient(type_, name, price)
    assert ingr.get_price() == price
