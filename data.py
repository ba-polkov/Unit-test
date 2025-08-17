from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestData:
    # Test data for buns
    BUN1_NAME = "black bun"
    BUN1_PRICE = 100
    BUN2_NAME = "white bun"
    BUN2_PRICE = 200

    # Test data for sauces
    SAUCE1_NAME = "hot sauce"
    SAUCE1_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE1_PRICE = 100
    SAUCE2_NAME = "sour cream"
    SAUCE2_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE2_PRICE = 200

    # Test data for fillings
    FILLING1_NAME = "cutlet"
    FILLING1_TYPE = INGREDIENT_TYPE_FILLING
    FILLING1_PRICE = 100
    FILLING2_NAME = "dinosaur"
    FILLING2_TYPE = INGREDIENT_TYPE_FILLING
    FILLING2_PRICE = 200

    # Expected values
    @staticmethod
    def burger_price(bun_price, *ingredients):
        return bun_price * 2 + sum(ingredients)