def test_get_name(ingredient_instance):
    ingredient, data = ingredient_instance
    assert ingredient.get_name() == data["name"]

def test_get_price(ingredient_instance):
    ingredient, data = ingredient_instance
    assert ingredient.get_price() == data["price"]

def test_get_type(ingredient_instance):
    ingredient, data = ingredient_instance
    assert ingredient.get_type() == data["type"]