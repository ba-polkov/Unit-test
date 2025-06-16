from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class DataBun:

    BUN_CREATION_TEST_DATA = [
        ("Краторная булка N-200i", 1255.0),
        ("Флюоресцентная булка R2-D3", 988.0)
    ]

class DataBurger:

    BUN_NAME = "Краторная булка N-200i"
    SAUCE_NAME = "Соус Spicy-X"
    SAUCE_TYPE = "sauce"
    MAIN_NAME = "Филе Люминесцентного тетраодонтимформа"
    MAIN_TYPE = "main"

    REMOVE_INGREDIENT_TEST_DATA = [
        (0, [MAIN_NAME, SAUCE_NAME]),
        (1, [SAUCE_NAME, SAUCE_NAME]),
        (2, [SAUCE_NAME, MAIN_NAME])
    ]

    MOVE_INGREDIENT_TEST_DATA = [
        (0, 1, ["ingredient2", "ingredient1", "ingredient3"]),
        (1, 0, ["ingredient2", "ingredient1", "ingredient3"]),
        (2, 0, ["ingredient3", "ingredient1", "ingredient2"]),
        (0, 2, ["ingredient2", "ingredient3", "ingredient1"]),
    ]

    GET_PRICE_TEST_DATA = [
        (100, [], 200),
        (50, [10], 110),
        (70, [20, 30, 40], 230),
        (100, [15.5, 20.5, 30.25], 266.25),
    ]

class DataIngredients:

    INGREDIENT_TEST_DATA = [
        # Стандартные случаи
        ("sauce", "Spicy Sauce", 90.0),
        ("main", "Beef Patty", 150.0),
        # Граничные случаи
        ("", "No Type", 60.0),  # Пустой тип
        ("sauce", "", 10.0),  # Пустое название
        ("main", "Free Ingredient", 0.0),  # Нулевая цена
        ("topping", "Cheddar", -5.0),  # Отрицательная цена
        ("long_type" * 10, "Long Name" * 10, 9999.99),  # Длинные строки
    ]

class DataDatabase:

    BUN_TEST_DATA = [
        (0, "black bun", 100),
        (1, "white bun", 200),
        (2, "red bun", 300)
    ]

    INGREDIENT_TEST_DATA = [
        (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]

class DataReceipt:

    RECEIPT = ["(==== Краторная булка N-200i ====)",
            "= sauce Соус Spicy-X =",
            "= main Филе Люминесцентного тетраодонтимформа =",
            "(==== Краторная булка N-200i ====)",
            "",
            f"Price: {3588.0}"]