def test_available_buns_returns_list(db):
    buns = db.available_buns()
    assert len(buns) == 3

def test_available_ingredients_returns_list(db):
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
