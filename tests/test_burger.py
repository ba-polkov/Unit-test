from praktikum.burger import Burger
from unittest.mock import Mock
from data.mock_burger import BUNS_INFO, INGREDIENTS_INFO, SELF_PRICE
import pytest

class TestBurger:
    
    @pytest.mark.parametrize("name", ['Japan bun', 'USA bun', 'Russia bun'])
    def test_set_buns(self, name):
        burger = Burger()
        assert burger.bun == burger.set_buns(name)
        
    @pytest.mark.parametrize("ingredient", ["Tomato", "Cheese", "Bacon"])
    def test_add_ingredient(self, ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]
        
    @pytest.mark.parametrize("ingredient_1, ingredient_2", [("Tomato", "Cheese")])
    def test_remove_ingredient(self, ingredient_1, ingredient_2):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ingredient_2]
        
    @pytest.mark.parametrize("ingredient_1, ingredient_2", [("Tomato", "Cheese")])
    def test_move_ingredient(self, ingredient_1, ingredient_2):
        burger = Burger()
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [ingredient_2, ingredient_1]
        
    def test_get_price(self):
        burger = Burger()
        m_bun = Mock()
        m_ingredient = Mock()
        
        m_bun.get_price.return_value = BUNS_INFO[0]['price']
        m_ingredient.get_price.return_value = INGREDIENTS_INFO[0]['price']
        
        burger.bun = m_bun
        burger.ingredients = [m_ingredient]
        
        assert burger.get_price() == BUNS_INFO[0]['price'] * 2 + INGREDIENTS_INFO[0]['price']
        
    def test_get_receipt(self):
        burger = Burger()
        m_bun = Mock()
        m_ingredient = Mock()
        m_price = Mock()
        
        m_bun.get_name.return_value = BUNS_INFO[0]['name']
        m_ingredient.get_name.return_value = INGREDIENTS_INFO[0]['name']
        m_ingredient.get_type.return_value = INGREDIENTS_INFO[0]['type']
        m_price.get_price.return_value = SELF_PRICE
        
        burger.bun = m_bun
        burger.ingredients = [m_ingredient]
        burger.get_price = m_price.get_price
        print(burger.get_receipt())
        
        assert burger.get_receipt() == (
            f'(==== {BUNS_INFO[0]["name"]} ====)\n'
            f'= filling {INGREDIENTS_INFO[0]["name"]} =\n'
            f'(==== {BUNS_INFO[0]["name"]} ====)\n\n'
            f'Price: {SELF_PRICE}'
        )
        
        
        
        
    