from data.data import Data
from praktikum.ingredient import Ingredient

class TestIngredient:
    # Проверяем, что метод корректно возвращает тип ингредиента
    def test_get_type_returns_correct_type(self):
        ingredient_data = Data.ingredients[0]
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])
        assert ingredient.get_type() == ingredient_data["type"]

    # Проверяем, что метод корректно возвращает название ингредиента
    def test_get_name_returns_correct_name(self):
        ingredient_data = Data.ingredients[1]
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])
        assert ingredient.get_name() == ingredient_data["name"]

    # Проверяем, что метод корректно возвращает цену ингредиента
    def test_get_price_returns_correct_price(self):
        ingredient_data = Data.ingredients[2]
        ingredient = Ingredient(ingredient_data["type"], ingredient_data["name"], ingredient_data["price"])
        assert ingredient.get_price() == ingredient_data["price"]
