from unittest.mock import patch
import pytest
from practikum.bun import Bun
from practikum.database import Database
from practikum.ingredient import Ingredient
from practikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Проверяем доступные булки через метод available_buns().
@pytest.mark.parametrize("bun_name_db, bun_price_db", [
                            ("black bun", 100),
                            ("white bun", 200),
                            ("red bun", 300)])
def test_available_buns(bun_name_db, bun_price_db):
    db = Database()
    buns = db.available_buns()
    for bun in buns:    # Для каждой булки в списке проверяем её имя и цену
        if bun.name == bun_name_db:
            assert bun.price == bun_price_db, "Метод available_buns возвращает неверную цену."

# Проверяем доступные ингредиенты через метод available_ingredients().
@pytest.mark.parametrize("ingredient_type, name, price", [
                            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                            (INGREDIENT_TYPE_FILLING, "cutlet", 100) ])
def test_available_ingredients(ingredient_type, name, price):
    db = Database()
    ingredients = db.available_ingredients()  # Получаем список доступных ингредиентов
    for ingredient in ingredients: # Для каждого ингредиента в списке проверяем его имя, тип и цену
        if ingredient.name == name:
            assert ingredient.type == ingredient_type, "Метод available_ingredients возвращает неверный тип."
            assert ingredient.price == price, "Метод available_ingredients возвращает неверную цену."


# Мокируем данные в Database, параметризуем эти данные
@pytest.mark.parametrize("mock_buns, mock_ingredients", [(
        [Bun("mocked bun 1", 50), Bun("mocked bun 2", 75)],
        [Ingredient(INGREDIENT_TYPE_SAUCE, "mocked sauce 1", 30), Ingredient(INGREDIENT_TYPE_FILLING, "mocked filling 1", 40)]
),
    (
        [Bun("mocked bun 3", 60)],
        [Ingredient(INGREDIENT_TYPE_SAUCE, "mocked sauce 2", 25)]
    )
])
@patch('practikum.database.Database.__init__', return_value=None)
def test_mocked_database_with_parametrize(mock_init, mock_buns, mock_ingredients):
    db = Database()
    db.buns = mock_buns
    db.ingredients = mock_ingredients

    # Проверяем, что метод available_buns возвращает правильные данные
    available_buns = db.available_buns()
    assert len(available_buns) == len(mock_buns), "Возвращаемое количество булок не соответствует заданному."
    for i in range(len(available_buns)):
        assert available_buns[i].name == mock_buns[i].name, "Метод available_buns возвращает неверное имя."
        assert available_buns[i].price == mock_buns[i].price, "Метод available_buns возвращает неверную цену."

    # Проверяем, что метод available_ingredients возвращает правильные данные
    available_ingredients = db.available_ingredients()
    assert len(available_ingredients) == len(mock_ingredients), "Возвращаемое количество ингредиентов не соответствует заданному."
    for i in range(len(available_ingredients)):
        assert available_ingredients[i].name == mock_ingredients[i].name, "Метод available_ingredients возвращает неверное имя."
        assert available_ingredients[i].type == mock_ingredients[i].type, "Метод available_ingredients возвращает неверный тип."
        assert available_ingredients[i].price == mock_ingredients[i].price, "Метод available_ingredients возвращает неверную цену."

