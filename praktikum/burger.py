from typing import List

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class Burger:
    """
    Модель бургера.
    Бургер состоит из булочек и ингредиентов (начинка или соус).
    Ингредиенты можно перемещать и удалять.
    Можно распечать чек с информацией о бургере.
    """

    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    def set_buns(self, bun: Bun):
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        # Удаляем элемент по index, затем вставляем его на new_index
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self) -> float:
        price = 0.0

        # УЛУЧШЕНИЕ: Защита от AttributeError, если bun == None
        if self.bun:
            price += self.bun.get_price() * 2

        for ingredient in self.ingredients:
            price += ingredient.get_price()

        return price

    def get_receipt(self) -> str:

        # ВАЖНО: Проверка на наличие булочек перед началом формирования чека
        if self.bun is None:
            raise ValueError("Булки не установлены. Невозможно создать чек.")

        receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']

        for ingredient in self.ingredients:
            # Используем .lower() для соответствия ожидаемому формату чека
            receipt.append(f'= {ingredient.get_type().lower()} {ingredient.get_name()} =')

        receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        receipt.append(f'Price: {self.get_price()}')

        return '\n'.join(receipt)