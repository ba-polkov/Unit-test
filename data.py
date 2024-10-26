from yandex import ingredient_types

class Buns:
    bun_name_1 = 'Флюоресцентная булка R2-D3'
    bun_name_2 = 'Краторная булка N-200i'
    bun_price_1 = 988
    bun_price_2 = 1255

class Ingredients:
    ingredient_name_1 = 'Соус Spicy-X'
    ingredient_name_2 = 'Соус фирменный Space Sauce'
    ingredient_name_3 = 'Мясо бессмертных моллюсков Protostomia'
    ingredient_name_4 = 'Говяжий метеорит (отбивная)'
    ingredient_price_1 = 90
    ingredient_price_2 = 80
    ingredient_price_3 = 1337
    ingredient_price_4 = 3000
    ingredient_type_1 = ingredient_types.INGREDIENT_TYPE_SAUCE
    ingredient_type_2 = ingredient_types.INGREDIENT_TYPE_FILLING

class Data:

    param = 'bun_name, bun_price, ingredient_type, ingredient_name, ingredient_price, expected_burger_price'
    value = [
        ['Булочка', 500, 'SAUSE', 'Острый', 50, 1050],
        ['super_bun', 200, 'FILLING', 'перец', 70, 470],
        ['1+1', 100, 'SAUSE', '', 0, 200],
        ['Лучший вариант', 300.57, '', '', 0, 601.14],
        ['The best', 592.15, 'FILLING', 'bam', 100.01, 1284.31]
    ]

    NAME_BUN = 'Тестовая'
    PRICE_BUN = 300
    NAME_INGREDIENT_1 = 'пикантный'
    PRICE_INGREDIENT_1 = 90
    NAME_INGREDIENT_2 = 'сырный'
    PRICE_INGREDIENT_2 = 50
    NAME_INGREDIENT_3 = 'грибы'
    PRICE_INGREDIENT_3 = 150
    RECEIPT = (f'(==== {NAME_BUN} ====)\n'
               f'= sauce {NAME_INGREDIENT_1} =\n'
               f'= filling {NAME_INGREDIENT_3} =\n'
               f'(==== {NAME_BUN} ====)\n'
               '\n'
               'Price: 840')