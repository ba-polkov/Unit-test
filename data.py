class BurgerConsist:
    FIRST_BUN_NAME = "white bun"
    SECOND_BUN_NAME = "red bun"
    FIRST_BUN_PRICE = 200.0
    SECOND_BUN_PRICE = 300.0

    INGREDIENT_TYPE_SAUCE = 'SAUCE'
    INGREDIENT_TYPE_SAUCE_NAME = "chili sauce"
    SAUCE_PRICE = 300.0

    INGREDIENT_TYPE_FILLING = 'FILLING'
    INGREDIENT_TYPE_FILLING_NAME = "dinosaur"
    FILLING_PRICE = 200.0


class BurgerGetPrice:
    TWO_BUNS_SAUCE_FILLING_PRICE = 900.0  # 2 булки и 2 ингредиента (соус и ингредиент)
    TWO_BUNS_PRICE = 400.0  # только булки
    BUNS_FILLING_PRICE = 700.0  # булки и ингредиент
    BUNS_SAUCE_PRICE = 700.0  # булки и соус

