class Ingredient:
    VALID_TYPES = ['FILLING', 'SAUCE', 'TOPPING']

    def __init__(self, ingredient_type, name, price):
        if ingredient_type not in self.VALID_TYPES:
            raise ValueError(f"Недопустимый тип ингредиента: {ingredient_type}")
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Название ингредиента должно быть непустой строкой")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена ингредиента должна быть положительным числом")

        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
