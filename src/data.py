from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

BUNS_DATA = [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
]

BUNS_WITH_NEGATIVE_PRICES = [
    ("black bun", -100.1),
    ("white bun", -200.2),
]

INGREDIENTS_DATA = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300)
]

INGREDIENTS_WITH_NEGATIVE_PRICES = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", -100.1),
    (INGREDIENT_TYPE_FILLING, "dinosaur", -200.2)
]