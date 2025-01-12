class Constants:
    BUN_NAME = "grey bun"
    BUN_PRICE = 10.0
    INGREDIENT_NAME_1 = "ketchup"
    INGREDIENT_NAME_2 = "meat cutlet"
    INGREDIENT_TYPE_1 = "sauce"
    INGREDIENT_TYPE_2 = "filling"
    INGREDIENT_PRICE_1 = 2.5
    INGREDIENT_PRICE_2 = 20.0
    BURGER_PRICE = BUN_PRICE * 2 + INGREDIENT_PRICE_1 + INGREDIENT_PRICE_2
    CREATE_RECEIPT = (
        f'(==== {BUN_NAME} ====)\n'
        f'= {INGREDIENT_TYPE_1} {INGREDIENT_NAME_1} =\n'
        f'= {INGREDIENT_TYPE_2} {INGREDIENT_NAME_2} =\n'
        f'(==== {BUN_NAME} ====)\n\n'
        f'Price: {BURGER_PRICE}'
    )
