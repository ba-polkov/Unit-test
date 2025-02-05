INGREDIENT_DATA = {
    "Биокотлета из марсианской Магнолии": {"type": "FILLING", "price": 424},
    "Филе Люминесцентного тетраодонтимформа": {"type": "FILLING", "price": 988},
    "Мясо бессмертных моллюсков": {"type": "FILLING", "price": 1337},
    "Говяжий метеорит (отбивная)": {"type": "FILLING", "price": 3000},
    "Хрустящие минеральные кольца": {"type": "FILLING", "price": 300},
    "Плоды Фалленианского дерева": {"type": "FILLING", "price": 874},
    "Кристаллы марсианских альфа-сахаридов": {"type": "FILLING", "price": 762},
    "Мини-салат Экзо-Плантаго": {"type": "FILLING", "price": 4400},
    "Сыр с астероидной плесенью": {"type": "FILLING", "price": 4142},
    "Соус Spicy-X": {"type": "SAUCE", "price": 90},
    "Соус фирменный Space Sauce": {"type": "SAUCE", "price": 80},
    "Соус традиционный галактический": {"type": "SAUCE", "price": 15},
    "Соус с шипами Антарианского плоскоходца": {"type": "SAUCE", "price": 88},
}

BUN_DATA = {
    "Краторная булка N-200i": {"price": 1255},
    "Флюоресцентная булка R2-D3": {"price": 988},
}

BUN_NAMES = list(BUN_DATA.keys())
INGREDIENT_NAMES = list(INGREDIENT_DATA.keys())
SAUCE_NAMES = [name for name in INGREDIENT_NAMES if INGREDIENT_DATA[name]["type"] == "SAUCE"]
FILLING_NAMES = [name for name in INGREDIENT_NAMES if INGREDIENT_DATA[name]["type"] == "FILLING"]