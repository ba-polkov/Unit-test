import sys
import os
import pytest
from unittest.mock import Mock

current_dir = os.path.dirname(__file__)
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from praktikum.burger import Burger


class TestBurger:
    
    def _create_bun_mock(self, name="black bun", price=100):
        bun = Mock()
        bun.get_name.return_value = name
        bun.get_price.return_value = price
        return bun
    
    def _create_ingredient_mock(self, ingredient_type="SAUCE", name="hot sauce", price=50):
        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        return ingredient
    
    def test_burger_initialization(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun_mock = self._create_bun_mock()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self):
        burger = Burger()
        ingredient_mock = self._create_ingredient_mock()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_mock

    def test_add_multiple_ingredients(self):
        burger = Burger()
        ingredient1 = self._create_ingredient_mock(name="sauce1")
        ingredient2 = self._create_ingredient_mock(name="sauce2")
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        
        assert len(burger.ingredients) == 2
        assert burger.ingredients == [ingredient1, ingredient2]

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient_mock = self._create_ingredient_mock()
        burger.add_ingredient(ingredient_mock)
        assert len(burger.ingredients) == 1
        
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_from_middle(self):
        burger = Burger()
        ingredients = [self._create_ingredient_mock(name=f"ingredient{i}") for i in range(3)]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients == [ingredients[0], ingredients[2]]

    def test_remove_ingredient_invalid_index(self):
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient(self):
        burger = Burger()
        ingredients = [self._create_ingredient_mock(name=f"ingredient{i}") for i in range(3)]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        
        burger.move_ingredient(1, 2)
        assert burger.ingredients == [ingredients[0], ingredients[2], ingredients[1]]

    def test_move_ingredient_invalid_index(self):
        burger = Burger()
        ingredient_mock = self._create_ingredient_mock()
        burger.add_ingredient(ingredient_mock)
        
        with pytest.raises(IndexError):
            burger.move_ingredient(1, 0)

    def test_move_ingredient_same_index(self):
        burger = Burger()
        ingredients = [self._create_ingredient_mock(name=f"ingredient{i}") for i in range(2)]
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        
        original_order = burger.ingredients.copy()
        burger.move_ingredient(0, 0)
        assert burger.ingredients == original_order

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", [
        (100, [50, 75], 325),      # 100*2 + 50 + 75 = 325
        (50, [25, 25, 25], 175),   # 50*2 + 25*3 = 175
        (200, [], 400),            # Только булочки: 200*2 = 400
        (0, [10, 20], 30),         # Бесплатные булочки: 0*2 + 10 + 20 = 30
        (150, [100], 400),         # 150*2 + 100 = 400
    ])
    def test_get_price_various_combinations(self, bun_price, ingredient_prices, expected_total):
        burger = Burger()
        bun_mock = self._create_bun_mock(price=bun_price)
        burger.set_buns(bun_mock)
        
        for price in ingredient_prices:
            ingredient_mock = self._create_ingredient_mock(price=price)
            burger.add_ingredient(ingredient_mock)
        
        assert burger.get_price() == expected_total

    def test_get_price_no_bun_raises_exception(self):
        burger = Burger()
        
        
        with pytest.raises(Exception):
            burger.get_price()

    def test_get_receipt_contains_required_elements(self):
        burger = Burger()
        bun_mock = self._create_bun_mock(name="black bun", price=100)
        burger.set_buns(bun_mock)
        
        sauce = self._create_ingredient_mock(ingredient_type="SAUCE", name="hot sauce", price=100)
        filling = self._create_ingredient_mock(ingredient_type="FILLING", name="cutlet", price=100)
        
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        
        receipt = burger.get_receipt()
        
        assert "black bun" in receipt
        assert "hot sauce" in receipt
        assert "cutlet" in receipt
        assert "400" in receipt  
        assert receipt.count("(====") == 2  
        assert "sauce" in receipt.lower()  
        assert "filling" in receipt.lower()

    def test_get_receipt_only_buns(self):
        burger = Burger()
        bun_mock = self._create_bun_mock(name="white bun", price=200)
        burger.set_buns(bun_mock)
        
        receipt = burger.get_receipt()
        
        assert "white bun" in receipt
        assert "400" in receipt  

    def test_get_receipt_no_bun_raises_exception(self):
        burger = Burger()
        
        with pytest.raises(Exception):
            burger.get_receipt()

    def test_get_receipt_ingredient_order_preserved(self):
        burger = Burger()
        bun_mock = self._create_bun_mock(name="red bun")
        burger.set_buns(bun_mock)
        
        ingredient1 = self._create_ingredient_mock(name="first")
        ingredient2 = self._create_ingredient_mock(name="second")
        ingredient3 = self._create_ingredient_mock(name="third")
        
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        
        receipt = burger.get_receipt()
        receipt_lines = receipt.split('\n')
        
  
        ingredient_lines = [line for line in receipt_lines if "=" in line and "====" not in line]
        assert "first" in ingredient_lines[0]
        assert "second" in ingredient_lines[1]
        assert "third" in ingredient_lines[2]