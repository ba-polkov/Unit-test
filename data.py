class BurgerElements:

    BUN_NAME_1 = "black bun"
    BUN_NAME_2 = "white bun"
    BUN_NAME_3 = "red bun"
    BUN_PRICE_1 = 100.0
    BUN_PRICE_2 = 200.0
    BUN_PRICE_3 = 300.0

    INGREDIENT_TYPE_1 = "SAUCE"
    SAUCE_NAME_1 = "hot sauce"
    SAUCE_NAME_2 = "sour cream"
    SAUCE_NAME_3 = "chili sauce"
    SAUCE_PRICE_1 = 100.0
    SAUCE_PRICE_2 = 200.0
    SAUCE_PRICE_3 = 300.0

    INGREDIENT_TYPE_2 = "FILLING"
    FILLING_NAME_1 = "cutlet"
    FILLING_NAME_2 = "dinosaur"
    FILLING_NAME_3 = "sausage"
    FILLING_PRICE_1 = 100.0
    FILLING_PRICE_2 = 200.0
    FILLING_PRICE_3 = 300.0

class IngredientIndex:

    FIRST_INGREDIENT = 0
    SECOND_INGREDIENT = 1
    THIRD_INGREDIENT = 2

class BurgerPrices:
    BURGER_PRICE_RED_BUNS = 300*2 #600, бургер с двумя красными булочками
    BURGER_PRICE_RB_CS_S = 300*2 + 300 + 300 #1200, бургер с двумя красными булочками, чили соусом и сосиской
    BURGER_PRICE_RB_HS_SC_D_S = 300*2 + 100 + 200 + 200 + 300 #1400, бургер с двумя красными булочками, острым соусом, сметаной, динозавром и сосиской
