def reorder_ingredients(ingredients, index, new_index):
    """Перемещает ингредиент в новый индекс."""
    ingredient = ingredients.pop(index)
    ingredients.insert(new_index, ingredient)
    return ingredients

def compare_buns(database, expected_buns):
    """Сравнивает булки из базы данных с ожидаемыми данными."""
    for index, bun_data in enumerate(expected_buns):
        bun = database.buns[index]
        if bun.name != bun_data["name"] or bun.price != bun_data["price"]:
            return False, f"Булка {index}: ожидалось {bun_data}, получено {{'name': {bun.name}, 'price': {bun.price}}}"
    return True, ""

def compare_ingredients(database, expected_ingredients):
    """Сравнивает ингредиенты из базы данных с ожидаемыми данными."""
    for index, ing_data in enumerate(expected_ingredients):
        ingredient = database.ingredients[index]
        if (ingredient.type != ing_data["type"] or
            ingredient.name != ing_data["name"] or
            ingredient.price != ing_data["price"]):
            return False, f"Ингредиент {index}: ожидалось {ing_data}, получено {{'type': {ingredient.type}, 'name': {ingredient.name}, 'price': {ingredient.price}}}"
    return True, ""
