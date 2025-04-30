from praktikum.burger import Burger
from praktikum.database import *

class MockBun:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price


class MockIngredient:
    def __init__(self, ingredient_type: str, name: str, price: float):
        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type



def test_set_buns():
    burger = Burger()
    bun = MockBun("Вкусная булочка", 159.50)
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient():
    burger = Burger()
    database = Database()
    ingredient = MockIngredient("FILLING", "Огурчики", 37.50)
    burger.add_ingredient(ingredient)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient


def test_remove_ingredient():
    burger = Burger()

    ingredient1 = MockIngredient("FILLING", "Лучок", 10.30)
    ingredient2 = MockIngredient("FILLING", "Помидор", 200.65)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient2


def test_move_ingredient():
    burger = Burger()

    ingredient1 = MockIngredient("FILLING", "Лучок", 29.50)
    ingredient2 = MockIngredient("SAUCE", "Кетчуп", 180.75)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ingredient2
    assert burger.ingredients[1] == ingredient1


def test_get_price():
    burger = Burger()
    bun = MockBun("Булочка для похудения", 100.50)
    ingredient1 = MockIngredient("FILLING", "Лук", 60)
    ingredient2 = MockIngredient("FILLING", "Лист салатный", 70)
    ingredient3 = MockIngredient("SAUCE", "Кетчуп", 24)
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)

    expected_price = bun.get_price() * 2 + ingredient1.get_price() + ingredient2.get_price() + ingredient3.get_price()
    assert burger.get_price() == expected_price


def test_get_receipt():

    bun = Bun(name="Булочка для похудения", price=100.59)
    ingredient1 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name="Лук", price=60)
    ingredient2 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name="Лист салатный", price=23.70)
    ingredient3 = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name="Кетчуп", price=15.3)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)


    expected_receipt = (
        '(==== Булочка для похудения ====)\n'
        '= filling Лук =\n'
        '= filling Лист салатный =\n'
        '= sauce Кетчуп =\n'
        '(==== Булочка для похудения ====)\n'
        '\nPrice: 300.18'
    )

    assert burger.get_receipt() == expected_receipt, f"Ожидался: {expected_receipt}, но получен: {burger.get_receipt()}"