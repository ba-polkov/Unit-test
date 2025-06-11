from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class BunData:

    list_buns = [
        ["black bun", 100],
        ["white bun", 200],
        ["red bun", 300]
    ]

class IngredientData:

    list_ingredient = [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [INGREDIENT_TYPE_FILLING, "sausage", 300]
    ]

class DatabaseBun:

    buns_data = [
        ["black bun", 100, 0],
        ["white bun", 200, 1],
        ["red bun", 300, 2]
    ]
