from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_burger_init_sets_bun_to_none_and_ingredients_to_empty_list(self):
        burger = Burger()
        assert burger.bun is None, \
            f"Ожидалось отсутствие булочки, получено '{burger.bun.name}'"
        assert burger.ingredients == [], \
            f"Ожидался пустой список ингридиентов, получен список из '{len(burger.ingredients)} 'ktvtynjd'"

    def test_set_buns_sets_bun_correctly(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, f"Ожидалось сохранение заданной булочки"

    def test_add_ingredient_increases_ingredients_list_length_by_one(self):
        burger = Burger()
        mock_ingredient = Mock()
        ingredients_count = len(burger.ingredients)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == ingredients_count+1, \
            f"Ожидалось увеличение на 1 кол-ва ингредиентов, было {ingredients_count}, стало {len(burger.ingredients)}"

    def test_add_ingredient_adds_correct_ingredient_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient, f"Ожидалось добавление заданного ингредиента"

    def test_remove_ingredient_reduces_list_length(self):
        burger = Burger()
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        ingredients_count = len(burger.ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == ingredients_count-1, \
            f"Ожидалось уменьшение на 1 кол-ва ингредиентов, было {ingredients_count}, стало {len(burger.ingredients)}"

    def test_remove_ingredient_keeps_correct_remaining_ingredient(self):
        burger = Burger()
        ing1 = Mock()
        ing2 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ing2, f"Ожидалось сохранение в списке нужного ингредиента"

    def test_move_ingredient_changes_order_correctly(self):
        burger = Burger()
        ing1 = Mock()
        ing2 = Mock()
        ing3 = Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [ing2, ing3, ing1], \
            f"Ожидалось корректное перемещение в списке заданного ингредиента"

    def test_get_price_with_bun_and_two_ingredients_calculates_correct_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        filling = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_price() == 100 * 2 + 50 + 150, f"Ожидалась цена бургера 400, а получена {burger.get_price()}"

    # Проверка имени верхней булочки рецепта
    def test_get_receipt_contains_upper_bun_name(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt.split('\n')[0], \
            f"Ожидалось корректное имя верхней булочки 'black bun'"

    def test_get_receipt_contains_ingredient_line(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        receipt = burger.get_receipt()
        assert "= sauce hot sauce" in receipt, \
            f"Ожидалось корректные тип и имя ингредиента в рецепте"

    # Проверка имени булочки внизу рецепта
    def test_get_receipt_contains_bottom_bun_name(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        assert "(==== black bun ====)" in lines[2], \
            f"Ожидалось корректное имя нижней булочки 'black bun'"

    def test_get_receipt_contains_total_price(self):
        burger = Burger()
        bun = Bun("black bun", 100)
        sauce = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        receipt = burger.get_receipt()
        assert "Price: 250" in receipt, f"Ожидалась корректная цена в рецепте"
