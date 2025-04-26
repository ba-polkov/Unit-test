from conftest import db


def get_bun_data(db):
    buns = db.available_buns()
    return [(bun.get_name(), bun.get_price()) for bun in buns]

def get_ingredient_data(db):
    ingredients = db.available_ingredients()
    return [(ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) for ingredient in ingredients]

def filter_by_type(ingredients, ingredient_type):
    return [ingredient for ingredient in ingredients if ingredient[0] == ingredient_type]

def get_price_dict(ingredients):
    return {ingredient[1]: ingredient[2] for ingredient in ingredients}

def calculate_burger_price(ingredients, mock_bun):
    ingredient_price = sum([ingredient.get_price() for ingredient in ingredients])
    burger_price = ingredient_price + (mock_bun.get_price()*2)
    return burger_price


