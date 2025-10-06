import pytest
from praktikum.ingredient import Ingredient
from data.data import ingredients_type_name_and_price

class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_and_price)
    def test_get_price_and_add_ingredient_check_price(self,ingredient_type, ingredient_name, ingredient_price):
        ing = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ing.get_price() == ingredient_price
        
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_and_price)
    def test_get_name_and_add_ingredient_check_name(self,ingredient_type, ingredient_name, ingredient_price):
        ing = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ing.get_name() == ingredient_name
        
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_and_price)
    def test_get_type_and_add_ingredient_check_type(self,ingredient_type, ingredient_name, ingredient_price):
        ing = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ing.get_type() == ingredient_type
                
                