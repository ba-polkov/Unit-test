import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def fresh_db():
    # Каждый тест получает новый экземпляр базы
    return Database()

def test_buns_are_returned_as_list(fresh_db):
    # Проверяем, что булочки выдаются списком
    buns = fresh_db.available_buns()
    assert isinstance(buns, list)

def test_ingredients_are_returned_as_list(fresh_db):
    # Проверяем, что ингредиенты тоже возвращаются списком
    items = fresh_db.available_ingredients()
    assert isinstance(items, list)

def test_buns_count_is_expected(fresh_db):
    # В базе ровно три вида булочек
    assert len(fresh_db.available_buns()) == 3

@pytest.mark.parametrize("i,expected", [
    (0, "black bun"),
    (1, "white bun"),
    (2, "red bun"),
])
def test_bun_names_are_correct(fresh_db, i, expected):
    # Названия булочек соответствуют списку
    buns = fresh_db.available_buns()
    assert buns[i].get_name() == expected

def test_ingredients_count_is_expected(fresh_db):
    # Проверяем количество ингредиентов
    assert len(fresh_db.available_ingredients()) == 6

@pytest.mark.parametrize("i,expected_type", [
    (0, INGREDIENT_TYPE_SAUCE),
    (3, INGREDIENT_TYPE_FILLING),
])
def test_ingredient_types_are_accurate(fresh_db, i, expected_type):
    # Тип ингредиента совпадает с ожидаемым
    items = fresh_db.available_ingredients()
    assert items[i].get_type() == expected_type
