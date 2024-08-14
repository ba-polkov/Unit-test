from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Constants:
    BUN_DATA = [
        ['First Bun', 200],
        ['Second Bun', 300]
    ]

    INGREDIENT_DATA = [
        [INGREDIENT_TYPE_SAUCE, 'First Ingredient', 20],
        [INGREDIENT_TYPE_FILLING, 'Second Ingredient', 30]
    ]

    BUN_AND_INGREDIENT_DATA = [
        ['First Bun', 200, INGREDIENT_TYPE_SAUCE, 'First Ingredient', 20, 420],
        ['Second Bun', 300, INGREDIENT_TYPE_FILLING, 'Second Ingredient', 30, 630]
    ]

    BUN_AND_FINAL_PRICE_DATA = [
        ['First Bun', 200, 450],
        ['Second Bun', 300, 650]
    ]
