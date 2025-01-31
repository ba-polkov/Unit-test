from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:
    bun_name = 'white bun'
    bun_price = 340
    bun_zero_price = 0.0
    bun_negative_price = -10.0
    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'hot sauce'
    sauce_price = 100
    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'cutlet'
    filling_price = 100
    burger_sum_price = bun_price * 2 + sauce_price + filling_price


class TestDataDB:
    test_data_buns = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]
    ]

    test_data_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]

    ]
