import pytest
from ..database import Database
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Проверяем, что база данных возвращает 3 булки
def test_database_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3
    assert all(hasattr(b, 'get_name') for b in buns)

# Проверяем, что база данных возвращает 6 ингредиентов
def test_database_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    assert all(hasattr(i, 'get_name') for i in ingredients)

# Проверяем, что имена всех булок присутствуют
@pytest.mark.parametrize("bun_name", ["black bun", "white bun", "red bun"])
def test_database_bun_names(bun_name):
    db = Database()
    names = [b.get_name() for b in db.available_buns()]
    assert bun_name in names

# Проверяем, что имена всех ингредиентов присутствуют
@pytest.mark.parametrize("ingredient_name", [
    "hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"
])
def test_database_ingredient_names(ingredient_name):
    db = Database()
    names = [i.get_name() for i in db.available_ingredients()]
    assert ingredient_name in names

# Проверяем, что типы всех ингредиентов присутствуют
@pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
def test_database_ingredient_types(ingredient_type):
    db = Database()
    types = [i.get_type() for i in db.available_ingredients()]
    assert ingredient_type in types
