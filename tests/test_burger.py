from unittest.mock import Mock
from praktikum.burger import Burger
from data import BURGER_DATA


class TestBurger:

    def test_empty_burger(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_set_buns(self):
        name, price = BURGER_DATA["test_set_buns"]

        burger = Burger()

        mock_bun = Mock()
        mock_bun.configure_mock(name=name)
        mock_bun.configure_mock(price=price)

        burger.set_buns(mock_bun)

        assert burger.bun.name == name and burger.bun.price == price

    def test_add_ingredient(self):
        type, name, price = BURGER_DATA["test_add_ingredient"]

        burger = Burger()

        mock_ingredient = Mock()
        mock_ingredient.configure_mock(type=type)
        mock_ingredient.configure_mock(name=name)
        mock_ingredient.configure_mock(price=price)

        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0].type == type and burger.ingredients[0].name == name and burger.ingredients[0].price == price

    def test_remove_ingredient(self):
        burger = Burger()

        mock_ingredient = [Mock(), Mock()]
        for i, ing in enumerate(mock_ingredient):
            ing.configure_mock(type=BURGER_DATA["test_remove_ingredient"][i]["type"])
            ing.configure_mock(name=BURGER_DATA["test_remove_ingredient"][i]["name"])
            ing.configure_mock(price=BURGER_DATA["test_remove_ingredient"][i]["price"])
        burger.ingredients = mock_ingredient

        burger.remove_ingredient(index=0)

        assert len(burger.ingredients) == 1 and burger.ingredients[0].name == BURGER_DATA["test_remove_ingredient"][1]["name"]

    def test_move_ingredient(self):
        burger = Burger()

        mock_ingredient = [Mock(), Mock(), Mock()]
        for i, ing in enumerate(mock_ingredient):
            ing.configure_mock(type=BURGER_DATA["test_move_ingredient"][i]["type"])
            ing.configure_mock(name=BURGER_DATA["test_move_ingredient"][i]["name"])
            ing.configure_mock(price=BURGER_DATA["test_move_ingredient"][i]["price"])
        burger.ingredients = mock_ingredient

        burger.move_ingredient(index=0, new_index=2)

        assert burger.ingredients[0].name == BURGER_DATA["test_move_ingredient"][1]["name"] and burger.ingredients[2].name == BURGER_DATA["test_move_ingredient"][0]["name"]

    def test_get_price(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        burger.bun = mock_bun

        mock_ingredient = [Mock(), Mock(), Mock()]
        for ing in mock_ingredient:
            ing.get_price.return_value = 10
        burger.ingredients = mock_ingredient

        assert burger.get_price() == 230

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = BURGER_DATA["test_get_receipt"]["bun_name"]
        burger.bun = mock_bun

        mock_ingredient = [Mock(), Mock()]
        ingredients = BURGER_DATA["test_get_receipt"]["ingredients"]
        for i, ing in enumerate(mock_ingredient):
            ing.get_type.return_value = ingredients[i]["type"]
            ing.get_name.return_value = ingredients[i]["name"]
        burger.ingredients = mock_ingredient

        mock_get_price = Mock(return_value=BURGER_DATA["test_get_receipt"]["total_price"])
        burger.get_price = mock_get_price

        assert burger.get_receipt() == BURGER_DATA["test_get_receipt"]["expected_result"]
