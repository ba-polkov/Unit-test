import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE

class TestBurger:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.burger = Burger()

    @pytest.fixture
    def bun_mock(self):
        return Mock(spec=Bun)

    @pytest.fixture
    def ingredient_mock(self):
        return Mock(spec=Ingredient)

    def test_set_buns(self, bun_mock):
        self.burger.set_buns(bun_mock)
        assert self.burger.bun == bun_mock

    def test_add_ingredient(self, ingredient_mock):
        self.burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in self.burger.ingredients

    def test_remove_ingredient(self, ingredient_mock):
        self.burger.add_ingredient(ingredient_mock)
        self.burger.remove_ingredient(0)
        assert ingredient_mock not in self.burger.ingredients

    def test_move_ingredient(self, ingredient_mock):
        ingredient_mock_2 = Mock(spec=Ingredient)
        self.burger.add_ingredient(ingredient_mock)
        self.burger.add_ingredient(ingredient_mock_2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[1] == ingredient_mock

    def test_get_price(self, bun_mock, ingredient_mock):
        bun_mock.get_price.return_value = 100
        ingredient_mock.get_price.return_value = 50
        self.burger.set_buns(bun_mock)
        self.burger.add_ingredient(ingredient_mock)
        # Цена: 2 * цена булки + цена ингредиента = 2*100 + 50 = 250
        assert self.burger.get_price() == 250

    def test_get_receipt(self, bun_mock, ingredient_mock):
        bun_mock.get_name.return_value = "black bun"
        bun_mock.get_price.return_value = 100
        ingredient_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient_mock.get_name.return_value = "hot sauce"
        ingredient_mock.get_price.return_value = 50

        self.burger.set_buns(bun_mock)
        self.burger.add_ingredient(ingredient_mock)

        expected_receipt = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "(==== black bun ====)\n\n"
            "Price: 250"
        )

        assert self.burger.get_receipt() == expected_receipt
