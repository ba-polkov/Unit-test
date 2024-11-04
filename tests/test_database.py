
def test_available_buns(database, buns_data):
    buns = database.available_buns()

    # Проверяем, что метод возвращает правильное количество булочек
    assert len(buns) == len(buns_data)

    # Проверяем, что каждая булочка имеет правильные свойства
    for bun, expected in zip(buns, buns_data):
        assert bun.get_name() == expected["name"]
        assert bun.get_price() == expected["price"]

def test_available_ingredients(database, ingredients_data):
    ingredients = database.available_ingredients()

    # Проверяем, что метод возвращает правильное количество ингредиентов
    assert len(ingredients) == len(ingredients_data)

    # Проверяем, что ингредиенты правильно инициализированы
    for ingredient, expected in zip(ingredients, ingredients_data):
        assert ingredient.get_type() == expected["type"]
        assert ingredient.get_name() == expected["name"]
        assert ingredient.get_price() == expected["price"]
