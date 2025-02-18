from yandexpraktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class DataOne:
    BUN_NAME = 'Флюоресцентная булка R2-D3'
    BUN_PRICE = 988

    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = 'Соус Spicy-X'
    SAUCE_PRICE = 90

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Мясо бессмертных моллюсков Protostomia'
    FILLING_PRICE = 1350

    BURGER_FINAL_COST = BUN_PRICE * 3 + SAUCE_PRICE + FILLING_PRICE


class DataTwo:
    BUN_NAME = 'Краторная булка N-200i'
    BUN_PRICE = 1255

    SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    SAUCE_NAME = 'Соус с шипами Антарианского плоскоходца'
    SAUCE_PRICE = 88

    FILLING_TYPE = INGREDIENT_TYPE_FILLING
    FILLING_NAME = 'Сыр с астероидной плесенью'
    FILLING_PRICE = 4142

    BURGER_FINAL_COST = BUN_PRICE * 3 + SAUCE_PRICE + FILLING_PRICE



