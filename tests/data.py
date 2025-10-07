"""
Модуль с тестовыми данными для всех тестов
"""


# Данные булочек
class BunData:
    BLACK_BUN = ("black bun", 100)
    WHITE_BUN = ("white bun", 200)
    RED_BUN = ("red bun", 300)


# Данные ингредиентов
class IngredientData:
    # Соусы
    HOT_SAUCE = ("SAUCE", "hot sauce", 100)
    SOUR_CREAM = ("SAUCE", "sour cream", 200)
    CHILI_SAUCE = ("SAUCE", "chili sauce", 300)

    # Начинки
    CUTLET = ("FILLING", "cutlet", 100)
    DINOSAUR = ("FILLING", "dinosaur", 200)
    SAUSAGE = ("FILLING", "sausage", 300)


# Ожидаемые результаты для тестов
class ExpectedResults:
    BURGER_PRICE_ONLY_BUN = 200
    BURGER_PRICE_WITH_INGREDIENTS = 400
    RECEIPT_WITH_INGREDIENTS = """(==== black bun ====)
= sauce hot sauce =
= filling cutlet =
(==== black bun ====)

Price: 400"""
    RECEIPT_WITHOUT_INGREDIENTS = """(==== white bun ====)
(==== white bun ====)

Price: 200"""