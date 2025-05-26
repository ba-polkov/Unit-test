class TestBunsData:
    BUNS = [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300)
    ]

    BUN = {'name': 'ordinary bun', 'price': 50}

class TestIngredientsData:
    INGREDIENTS = [
        ('SAUCE', 'hot sauce', 100),
        ('SAUCE', 'sour cream', 200),
        ('SAUCE', 'chili sauce', 300),
        ('FILLING', 'cutlet', 100),
        ('FILLING', 'dinosaur', 200),
        ('FILLING', 'sausage', 300)
    ]

    INGREDIENT = {'ingredient_type': 'SAUCE', 'name': 'BBQ', 'price': 150}

    SAUCE = {'ingredient_type': 'SAUCE', 'name': 'hot sauce', 'price': 100}
    FILLING = {'ingredient_type': 'FILLING', 'name': 'dinosaur', 'price': 200}

class TestReceipt:
    BUN_NAME = '(==== ordinary bun ====)'
    SAUCE_NAME = '= sauce hot sauce ='
    FILLING_NAME = '= filling dinosaur ='
    RECEIPT_PRICE = '\nPrice: 400'
    EXPECTED_RECEIPT = '\n'.join([BUN_NAME, SAUCE_NAME, FILLING_NAME, BUN_NAME,  RECEIPT_PRICE])
