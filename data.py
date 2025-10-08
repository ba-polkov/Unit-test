BUN_DATA = {
    "test_bun_name": ["Краторная булка N-200i", 1255],
    "test_bun_price_positive": ["Флюоресцентная булка R2-D3", 1255],
    "test_bun_price_float": ["Краторная булка N-200i", 1255.55]
}

INGREDIENTS_DATA = {
    "test_ingredients_type": ["SAUCE", "Соус Spicy-X", 90],
    "test_ingredients_name": ["FILLING", "Мини-салат Экзо-Плантаго", 4400],
    "test_ingredients_price_positive": ["SAUCE", "Соус с шипами Антарианского плоскоходца", 88],
    "test_ingredients_price_float": ["FILLING", "Говяжий метеорит (отбивная)", 3000.099]
}

BURGER_DATA = {
    "test_set_buns": ["Флюоресцентная булка R2-D3", 1255],
    "test_add_ingredient": ["SAUCE", "Соус Spicy-X", 90],
    "test_remove_ingredient": [{"type": "FILLING", "name": "Мини-салат Экзо-Плантаго", "price": 4400},
                               {"type": "SAUCE", "name": "Соус с шипами Антарианского плоскоходца", "price": 88}],
    "test_move_ingredient": [{"type": "SAUCE", "name": "Соус Spicy-X", "price": 90},
                             {"type": "FILLING", "name": "Мини-салат Экзо-Плантаго", "price": 4400},
                             {"type": "SAUCE", "name": "Соус с шипами Антарианского плоскоходца", "price": 88}],
    "test_get_receipt": {"bun_name": "Краторная булка N-200i",
                         "ingredients": [{"name": "Говяжий метеорит (отбивная)", "type": "FILLING"},
                                         {"name": "Соус с шипами Антарианского плоскоходца", "type": "SAUCE"}],
                         "total_price": 9999.99,
                         "expected_result": "(==== Краторная булка N-200i ====)\n= filling Говяжий метеорит (отбивная) =\n= sauce Соус с шипами Антарианского плоскоходца =\n(==== Краторная булка N-200i ====)\n\nPrice: 9999.99"}
}

DATABASE_DATA = {
    "test_available_buns_total_len": 3,
    "test_available_buns": [[0, "black bun", 100], [1, "white bun", 200], [2, "red bun", 300]],
    "test_available_ingredients_len": 6,
    "test_available_ingredients": [[0, "SAUCE", "hot sauce", 100], [1, "SAUCE", "sour cream", 200], [2, "SAUCE", "chili sauce", 300],
                                   [3, "FILLING", "cutlet", 100], [4, "FILLING", "dinosaur", 200], [5, "FILLING", "sausage", 300]]
}
