from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

#Проверка, что булочка в бургере создана, и ее имя соответствует тестовым данным
    def test_set_buns_input_test_name_output_test_name(self):
        mock_bun = Mock()
        mock_bun.name = 'Mike'
        mock_bun.price = 600
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == 'Mike'

#Проверка, что булочка в бургере создана, и ee цена соответствует тестовым данным
    def test_set_buns_input_test_price_output_test_price(self):
        mock_bun = Mock()
        mock_bun.name = 'Mike'
        mock_bun.price = 500
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.price == 500

#Проверка, что добавленный ингредиент соответствует тестовым данным
    def test_add_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_FILLING
        mock_ingredient.name = 'Наполнитель'
        mock_ingredient.price = 50
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert (burger.ingredients[0].type == ingredient_types.INGREDIENT_TYPE_FILLING and
                burger.ingredients[0].name == 'Наполнитель' and burger.ingredients[0].price == 50)

#Проверка, что после добавления нового ингредиента, ингредиентов в списке стало два
    def test_add_ingredient_add_second_ingredient_total_two_ingredients(self):
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_FILLING
        mock_ingredient.name = 'Наполнитель'
        mock_ingredient.price = 50
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 2

#Проверка, что после удаления ингредиента, ингредиент в списке остался один
    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_FILLING
        mock_ingredient.name = 'Наполнитель'
        mock_ingredient.price = 50
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 1

#Проверка, что после смещения ингредиентов их индексы сменились
    def test_move_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_FILLING
        mock_ingredient.name = 'Наполнитель'
        mock_ingredient.price = 50
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = 'Соус'
        mock_ingredient.price = 60
        burger.add_ingredient(mock_ingredient)

        burger.move_ingredient(1, 0)

        assert (burger.ingredients[0].type == ingredient_types.INGREDIENT_TYPE_SAUCE and
                burger.ingredients[0].name == 'Соус' and burger.ingredients[0].price == 60)

#Проверка, что после смещения ингредиентов их количество осталось равным 2
    def test_move_ingredient_before_two_ingredients_after_two_ingredients(self):
        mock_ingredient = Mock()
        mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_FILLING
        mock_ingredient.name = 'Наполнитель'
        mock_ingredient.price = 50
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = 'Соус'
        mock_ingredient.price = 60
        burger.add_ingredient(mock_ingredient)

        burger.move_ingredient(1, 0)

        assert len(burger.ingredients) == 2

    def test_get_price(self):
        mock_bun = Mock()
        #mock_bun.name = 'Mike'
        #mock_bun.price = 500
        mock_bun.get_price.return_value = 500
        burger = Burger()
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        #mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_SAUCE
        #mock_ingredient.name = 'Соус'
        mock_ingredient.price = 60
        mock_ingredient.get_price.return_value = 60

        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 1060

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()

        mock_bun.get_price.return_value = 500
        mock_bun.get_name.return_value = 'Mike'
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 60
        mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = 'Соус'
        burger.add_ingredient(mock_ingredient)

        assert burger.get_receipt() == '(==== Mike ====)\n= sauce Соус =\n(==== Mike ====)\n\nPrice: 1060'
