import pytest
from unittest.mock import MagicMock
from ya_praktikum.bun import Bun
from ya_praktikum.ingredient import Ingredient
from ya_praktikum.burger import Burger
from ya_praktikum.database import Database
from ya_praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

#Фикстура для создания тестовой булочки
@pytest.fixture
def sample_bun():
    return Bun(name="white", price=25)

#Фикстуры для теста бургера
@pytest.fixture
def bun():
    return Bun("White Bun", 25)

@pytest.fixture
def ingredient():
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = "lettuce"
    ingredient.get_price.return_value = 1
    ingredient.get_type.return_value = "topping"
    return ingredient

@pytest.fixture
def ingredient2():
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = "Tomato"
    ingredient.get_price.return_value = 2
    ingredient.get_type.return_value = "topping"
    return ingredient

#Создает экземпляр Burger с установленной булочкой White Bun
@pytest.fixture
def burger_with_bun(bun):
    burger = Burger()
    burger.set_buns(bun)
    return burger


# Фикстуры для теста данных
@pytest.fixture
def buns_data():
    return [
        {"name": "black bun", "price": 100},
        {"name": "white bun", "price": 200},
        {"name": "gluten-free", "price": 300},
    ]


@pytest.fixture
def ingredients_data():
    return [
        {"type": INGREDIENT_TYPE_SAUCE, "name": "spicy mayo", "price": 100},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "garlic aioli", "price": 200},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "barbecue sauce", "price": 300},
        {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
        {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
        {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300},
    ]


@pytest.fixture
def database(buns_data, ingredients_data):
    db = Database()
    db.buns = [Bun(data["name"], data["price"]) for data in buns_data]
    db.ingredients = [
        Ingredient(data["type"], data["name"], data["price"]) for data in ingredients_data
    ]

    return db

#Фикстуры для теста ингридиентов
@pytest.fixture(params=[
    (INGREDIENT_TYPE_SAUCE, "barbecue sauce", 50),
    (INGREDIENT_TYPE_SAUCE, "mustard", 30),
    (INGREDIENT_TYPE_FILLING, "chicken", 100),
    (INGREDIENT_TYPE_FILLING, "bacon", 20),
])
def ingredient_data(request):
    return request.param
