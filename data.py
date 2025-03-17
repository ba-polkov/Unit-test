class IngredientData:
    ing_type = 'SAUCE'
    ing_name = 'Неизвестная жидкость'
    ing_price = 100.33

class BunData:
    bun_name = 'Крафтовая булка'
    bun_price = 2.55

class BurgerData:
    bun = {'name':"white bun", 'price': 200}
    ing_1 = {'type': 'SAUCE', 'name': "hot sauce", 'price': 100}
    ing_2 = {'type': 'FILLING', 'name': "cutlet", 'price': 100}
    total_price = bun.get('price') * 2 + ing_1.get('price') + ing_2.get('price')
    receipt_model = [f'(==== {bun.get('name')} ====)',
            f'= {ing_1.get('type').lower()} {ing_1.get('name')} =',
            f'= {ing_2.get('type').lower()} {ing_2.get('name')} =',
            f'(==== {bun.get('name')} ====)\n',
            f'Price: {str(total_price)}']
