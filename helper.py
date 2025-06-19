from unittest.mock import Mock
from practicum_burgers.bun import Bun
from practicum_burgers.ingredient import Ingredient



def create_and_set_bun_mock(burger, price=50, name="Булка"):
    bun_mock = Mock(spec=Bun)
    bun_mock.get_price.return_value = price
    bun_mock.get_name.return_value = name
    burger.set_buns(bun_mock)
    return bun_mock

def create_and_add_ingredients_mock(burger, ingredient_type = 'SAUCE', price=30, name="Сыр"):
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_type.return_value = ingredient_type
    ingredient_mock.get_price.return_value = price
    ingredient_mock.get_name.return_value = name
    burger.add_ingredient(ingredient_mock)
    return ingredient_mock

