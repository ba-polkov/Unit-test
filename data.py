class BunData:
    BUN_NAMES = [
        "Марсианка",
        "Луна",
        "Центр Вселенной"
    ]

    BUN_PRICES = [
        257,
        155,
        1000
    ]

class IngredientData:
    INGREDIENT_TYPES = [
        "SAUCE",
        "FILLING"
    ]

    INGREDIENT_NAMES = [
        "Вулканическая пыль",
        "Филе единорога"
    ]

    INGREDIENT_PRICES = [
        355,
        1557
    ]

class MockBurger:
    BUN_NAME = "Марсианка"
    BUN_PRICE = 257
    FILLING_PRICE  = 424
    FILLING_NAME = "Биокотлета из марсианской Магнолии"
    FILLING_TYPE = "FILLING"
    SAUCE_PRICE = 15
    SAUCE_NAME = "Соус традиционный галактический"
    SAUCE_TYPE = "SAUCE"
    EXPECTED_RECEIPT = '(==== Марсианка ====)\n= filling Биокотлета из марсианской Магнолии =\n= sauce Соус традиционный галактический =\n(==== Марсианка ====)\n\nPrice: 953'