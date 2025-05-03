from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


class TestBurger:

#Проверка, что булочка в бургере создана, и ее имя соответствует тестовым данным
    def test_set_buns_input_test_name_output_test_name(self, bun, burger):
        burger = burger
        burger.set_buns(bun)

        assert burger.bun.name == 'Mike'

#Проверка, что булочка в бургере создана, и ee цена соответствует тестовым данным
    def test_set_buns_input_test_price_output_test_price(self, bun, burger):
        burger = burger
        burger.set_buns(bun)

        assert burger.bun.price == 500

#Проверка, что добавленный ингредиент соответствует тестовым данным
    def test_add_ingredient(self, burger):
        burger = burger
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'Наполнитель', 50)
        burger.add_ingredient(ingredient)

        assert (burger.ingredients[1].type == ingredient_types.INGREDIENT_TYPE_FILLING and
                burger.ingredients[1].name == 'Наполнитель' and burger.ingredients[1].price == 50)

#Проверка, что после добавления нового ингредиента, ингредиентов в списке стало два
    def test_add_ingredient_add_second_ingredient_total_two_ingredients(self, burger):
        burger = burger
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'Наполнитель', 50)
        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 2

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
