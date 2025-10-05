class TestData:
    # Валидные булки (name, price)
    valid_buns = [
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988)
    ]
    
    # Невалидные булки (name, price)
    invalid_buns = [
        ("", -100),          # Пустое название + отрицательная цена
        ("   ", 0),          # Пробелы вместо названия + нулевая цена
        (123, 100),          # Неверный тип названия
        ("Булка", -0.01)     # Дробная отрицательная цена
    ]
    
    # Валидные ингредиенты (type, name, price)
    valid_ingredients = [
        ("FILLING", "Биокотлета из марсианской Магнолии", 424),
        ("SAUCE", "Соус Spicy-X", 90),
        ("TOPPING", "Сыр с астероидной плесенью", 4142)
    ]
    
    # Невалидные ингредиенты (type, name, price)
    invalid_ingredients = [
        ("INVALID_TYPE", "Невалидный ингредиент", 100),  # Неправильный тип
        ("SAUCE", "", -50),                              # Пустое название
        (123, "Ингредиент", 100),                        # Неверный тип названия
        ("TOPPING", "Сыр", 0)                            # Нулевая цена
    ]
    
    # Тест-кейсы для бургеров (bun_data, ingredients_data, expected)
    burger_cases = [
        # Валидные кейсы
        (valid_buns[0], [valid_ingredients[0]], 1255*2 + 424),
        (valid_buns[1], valid_ingredients[1:], 988*2 + 90 + 4142),
        (valid_buns[0], [], 1255*2),
        
        # Невалидные кейсы (ожидаем исключение)
        (invalid_buns[0], [valid_ingredients[0]], ValueError),
        (valid_buns[0], [invalid_ingredients[0]], ValueError)
    ]
