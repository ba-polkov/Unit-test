from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class Data1:
    bun_name = 'Флюоресцентная булка R2-D3'
    bun_price = 988

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус традиционный галактический'
    sauce_price = 15

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Мясо бессмертных моллюсков Protostomia'
    filling_price = 1350

    burger_final_cost = bun_price * 2 + sauce_price + filling_price
    
class Data2:
    bun_name = 'Краторная булка N-200i'
    bun_price = 1255

    sauce_type = INGREDIENT_TYPE_SAUCE
    sauce_name = 'Соус с шипами Антарианского плоскоходца'
    sauce_price = 88

    filling_type = INGREDIENT_TYPE_FILLING
    filling_name = 'Сыр с астероидной плесенью'
    filling_price = 4142

    burger_final_cost = bun_price * 2 + sauce_price + filling_price
    