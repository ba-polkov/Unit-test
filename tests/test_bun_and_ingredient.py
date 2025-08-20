import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

"""
Не совсем понятная формулировка задания, но на всякий случай сделаю покрытие всего кода проекта тестами.
"""

def test_bun_getters():
    
    bun = Bun('black bun', 100)
    assert bun.get_name() == 'black bun'
    assert bun.get_price() == 100


@pytest.mark.parametrize(
    "itype,name,price",
    [
        (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
        (INGREDIENT_TYPE_FILLING, 'sausage', 300),
    ],
)
def test_ingredient_getters(itype, name, price):
    ing = Ingredient(itype, name, price)
    # Проверяем, что геттеры отдают ровно то, что передали в конструктор
    assert ing.get_type() == itype
    assert ing.get_name() == name
    assert ing.get_price() == price