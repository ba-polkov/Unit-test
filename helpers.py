from typing import List
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def get_bun_names(buns: List[Bun]) -> List[str]:
    return [bun.get_name() for bun in buns]

def get_ingredient_names(ingredients: List[Ingredient]) -> List[str]:
    return [ingredient.get_name() for ingredient in ingredients]