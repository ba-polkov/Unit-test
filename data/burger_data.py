import data.ingredient_types as ingredient_types


class IngredientsData:

    SAUCE_1 = (ingredient_types.INGREDIENT_TYPE_SAUCE, 'кетчуп', 1.1)
    SAUCE_2 = (ingredient_types.INGREDIENT_TYPE_SAUCE, 'майонез', 0.8)

    FILLING_1 = (ingredient_types.INGREDIENT_TYPE_FILLING, 'сыр', 2.5)
    FILLING_2 = (ingredient_types.INGREDIENT_TYPE_FILLING, 'котлета', 2.9)

    DB_BUNS_NAMES = ["black bun", "white bun", "red bun"]
    DB_BUNS_PRICES = [100, 200, 300]

    DB_SAUCES = ["hot sauce", "sour cream", "chili sauce"]
    DB_FILLINGS = ["cutlet", "dinosaur", "sausage"]


class BunsData:

    BUN_1 = ("Булка с кунжутом", 1.0)
    BUN_2 = ("Ржаная булка", 10)
    BUN_3 = ("Булка-булка", 0.5)
