from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# список булок для тестов класса Bun
buns_name_and_price = [
    ["Булка Плазменная Z-12", 1234.0],
    ["Булка Сингулярности Vortex", 1111.0],
    ["Булка Хроноворот", 999.0]
]

# список ингредиентов с типом, названием и ценой для тестов класса Ingredient
ingredients_type_name_and_price = [
    [INGREDIENT_TYPE_SAUCE, "Соус Антиматерии", 95.0],
    [INGREDIENT_TYPE_SAUCE, "Соус Квантовый", 85.0],
    [INGREDIENT_TYPE_SAUCE, "Соус Туманности", 25.0],
    [INGREDIENT_TYPE_FILLING, "Филе Звёздного Китa", 1450.0],
    [INGREDIENT_TYPE_FILLING, "Мясо Андроидов", 2999.0],
    [INGREDIENT_TYPE_FILLING, "Тофу из Тёмной Энергии", 510.0],
]

# список булок для тестирования базы данных
expected_buns = [
        [0, "black bun", 100],
        [1, "white bun", 200],
        [2, "red bun", 300],
    ]
# список ингредиентов для тестирования базы данных
expected_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
        [1, INGREDIENT_TYPE_SAUCE, "sour cream", 200],
        [2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [3, INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [4, INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [5, INGREDIENT_TYPE_FILLING, "sausage", 300]
    ]