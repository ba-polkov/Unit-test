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

    def test_remove_ingredient(self, burger):
        burger = burger
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'Наполнитель', 50)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 1

    def test_move_ingredient(self, burger):
        burger = burger
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'Наполнитель', 50)
        burger.add_ingredient(ingredient)
        burger.move_ingredient(1, 0)

        assert (burger.ingredients[0].type == ingredient_types.INGREDIENT_TYPE_FILLING and
                burger.ingredients[0].name == 'Наполнитель' and burger.ingredients[0].price == 50)

    def test_get_price(self, burger):
        burger = burger

        assert burger.get_price() == 1060

    def test_get_receipt(self, burger):
        burger = burger
        print(burger.get_receipt())

        assert burger.get_receipt() == '(==== Mike ====)\n= sauce Соус =\n(==== Mike ====)\n\nPrice: 1060'
