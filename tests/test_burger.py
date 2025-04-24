import pytest
from ..burger import Burger

# Вспомогательные классы-заглушки необходимы для изоляции тестов

# Вспомогательный класс-заглушка для булочки
class DummyBun:
    def get_price(self):
        return 50
    def get_name(self):
        return "Test Bun"

# Вспомогательный класс-заглушка для ингредиента
class DummyIngredient:
    def __init__(self, name, price, type_):
        self._name = name
        self._price = price
        self._type = type_
    def get_price(self):
        return self._price
    def get_name(self):
        return self._name
    def get_type(self):
        return self._type

# Фикстура для создания пустого бургера
@pytest.fixture
def burger():
    return Burger()

# Проверяем расчет цены с разными наборами ингредиентов
@pytest.mark.parametrize("ingredients,expected_price", [
    ([DummyIngredient("A", 10, "SAUCE")], 50*2+10),
    ([DummyIngredient("A", 10, "SAUCE"), DummyIngredient("B", 20, "FILLING")], 50*2+10+20),
])
def test_burger_price(burger, ingredients, expected_price):
    burger.set_buns(DummyBun())
    for ing in ingredients:
        burger.add_ingredient(ing)
    assert burger.get_price() == expected_price

# Проверяем добавление, перемещение и удаление ингредиентов
def test_burger_add_remove_move_ingredient(burger):
    burger.set_buns(DummyBun())
    ing1 = DummyIngredient("A", 10, "SAUCE")
    ing2 = DummyIngredient("B", 20, "FILLING")
    ing3 = DummyIngredient("C", 30, "FILLING")
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.add_ingredient(ing3)
    burger.move_ingredient(2, 0)
    assert burger.ingredients[0] == ing3
    burger.remove_ingredient(1)
    assert len(burger.ingredients) == 2

# Проверяем корректность чека
def test_burger_receipt(burger):
    burger.set_buns(DummyBun())
    ing = DummyIngredient("A", 10, "SAUCE")
    burger.add_ingredient(ing)
    receipt = burger.get_receipt()
    assert "Test Bun" in receipt
    assert "a A" in receipt or "A" in receipt
    assert "Price: 110" in receipt
