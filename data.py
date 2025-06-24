from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# булка для тестирования
bun_name_price = ("Булочка марсианская", 999)
# ингредиент для тестирования
ingredient_sauce = ("SAUCE", "hot sauce", 100)

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