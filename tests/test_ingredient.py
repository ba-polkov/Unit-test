
def test_ingredient_creation(ketchup):
    assert ketchup.type == 'SAUCE'
    assert ketchup.name == 'Кетчуп'
    assert ketchup.price == 3.50

def test_get_price_ingredient(ketchup):
    assert ketchup.get_price() == 3.50

def test_get_name_ingredient(ketchup):
    assert ketchup.get_name() == 'Кетчуп'

def test_get_type_ingredient(cucumber):
    assert cucumber.type == 'FILLING'