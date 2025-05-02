from ingredient import Ingredient
import ingredient_types


class TestBurger:


    def test_set_buns(self, bun, burger):
        burger = burger
        burger.set_buns(bun)

        assert burger.bun.name == 'Mike'

    def test_add_ingredient(self, burger):
        burger = burger
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'Наполнитель', 50)
        burger.add_ingredient(ingredient)

        assert (burger.ingredients[1].type == ingredient_types.INGREDIENT_TYPE_FILLING and
                burger.ingredients[1].name == 'Наполнитель' and burger.ingredients[1].price == 50)