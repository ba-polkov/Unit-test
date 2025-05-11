import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Тест на инициализацию ингредиента
def test_ingredient_initialization():
    # Создаём ингредиент
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

    # Проверяем, что тип, имя и цена корректно установлены
    assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
    assert ingredient.get_name() == "hot sauce"
    assert ingredient.get_price() == 100


# Тест на тип ингредиента
@pytest.mark.parametrize(
    "ingredient_type, expected_type",
    [
        (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING),
    ]
)
def test_ingredient_type(ingredient_type, expected_type):
    # Создаём ингредиент с параметризированным типом
    ingredient = Ingredient(ingredient_type, "some ingredient", 150)

    # Проверяем, что тип ингредиента соответствует ожидаемому
    assert ingredient.get_type() == expected_type


# Тест на имя ингредиента
@pytest.mark.parametrize(
    "name, expected_name",
    [
        ("hot sauce", "hot sauce"),
        ("cutlet", "cutlet"),
        ("chili sauce", "chili sauce"),
    ]
)
def test_ingredient_name(name, expected_name):
    # Создаём ингредиент с параметризированным именем
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)

    # Проверяем, что имя ингредиента соответствует ожидаемому
    assert ingredient.get_name() == expected_name


# Тест на цену ингредиента
@pytest.mark.parametrize(
    "price, expected_price",
    [
        (100, 100),
        (200, 200),
        (300, 300),
    ]
)
def test_ingredient_price(price, expected_price):
    # Создаём ингредиент с параметризированной ценой
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", price)

    # Проверяем, что цена ингредиента соответствует ожидаемой
    assert ingredient.get_price() == expected_price