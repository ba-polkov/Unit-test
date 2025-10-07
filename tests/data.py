from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

# Список тестовых булок
BUNS = [
    Bun("black bun", 100),
    Bun("white bun", 200),
    Bun("red bun", 300),
]

# Список тестовых ингредиентов
INGREDIENTS = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 10),
    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 50),
    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 40),
    Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 5),
    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 60),
]