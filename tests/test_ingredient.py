import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [ # Параметризация для проверки различных значений типа, имени и цены ингредиента
        ("sauce", "hot sauce", 100.0),
        ("filling", "cutlet", 150.0),
        ("sauce", "sour cream", 200.0),
        ("filling", "dinosaur", 250.0),
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price): # Проверяем, что ингредиент инициализируется с правильными значениями
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_get_price(self): # Проверяем, что метод возвращает правильную цену
        ingredient = Ingredient("sauce", "hot sauce", 100.0)
        assert ingredient.get_price() == 100.0

    def test_get_name(self): # Проверяем, что метод возвращает правильное имя
        ingredient = Ingredient("filling", "cutlet", 150.0)
        assert ingredient.get_name() == "cutlet"

    def test_get_type(self): # Проверяем, что метод возвращает правильный тип
        ingredient = Ingredient("sauce", "hot sauce", 100.0)
        assert ingredient.get_type() == "sauce"
