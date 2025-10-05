class Bun:
    def __init__(self, name, price):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Название булки должно быть непустой строкой")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена булки должна быть положительным числом")
        
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price
