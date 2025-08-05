from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_database_available_buns():
    """
    Проверяет корректность списка булок
    """
    db = Database()
    buns = db.available_buns()
    
    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[0].get_price() == 100
    assert buns[1].get_name() == "white bun"
    assert buns[1].get_price() == 200
    assert buns[2].get_name() == "red bun"
    assert buns[2].get_price() == 300


def test_database_available_ingredients():
    """
    Проверяет корректность списка ингредиентов
    """
    db = Database()
    ingredients = db.available_ingredients()
    
    assert len(ingredients) == 6
    
    # Проверка соусов
    for i in range(3):
        assert ingredients[i].get_type() == INGREDIENT_TYPE_SAUCE
    
    # Проверка начинок
    for i in range(3, 6):
        assert ingredients[i].get_type() == INGREDIENT_TYPE_FILLING
    
    # Проверка конкретных значений
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[3].get_name() == "cutlet"
    assert ingredients[2].get_price() == 300
    assert ingredients[5].get_price() == 300