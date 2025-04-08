import pytest
from Diplom_1.ingredient import Ingredient


class TestIngredient():
    @pytest.mark.parametrize(
        "type, name, price, expected_price",
        [
            ('SAUCE', "hot sauce", 100, 100),
            ('SAUCE', "sour cream", 200, 200),
            ('SAUCE', "chili sauce", 300, 300),
            ('FILLING', "cutlet", 100, 100),
            ('FILLING', "dinosaur", 200, 200),
            ('FILLING', "sausage", 300, 300)
        ]
    )
    def test_get_price(self, type, name, price, expected_price):
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_price() == expected_price


    @pytest.mark.parametrize(
        "type, name, price, expected_name",
        [
            ('SAUCE', "hot sauce", 100, "hot sauce"),
            ('SAUCE', "sour cream", 200, "sour cream"),
            ('SAUCE', "chili sauce", 300, "chili sauce"),
            ('FILLING', "cutlet", 100, "cutlet"),
            ('FILLING', "dinosaur", 200, "dinosaur"),
            ('FILLING', "sausage", 300, "sausage")
        ]
    )
    def test_get_name(self, type, name, price, expected_name):
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_name()==expected_name


    @pytest.mark.parametrize(
        "type, name, price, expected_type",
        [
            ('SAUCE', "hot sauce", 100, 'SAUCE'),
            ('SAUCE', "sour cream", 200, 'SAUCE'),
            ('SAUCE', "chili sauce", 300, 'SAUCE'),
            ('FILLING', "cutlet", 100, 'FILLING'),
            ('FILLING', "dinosaur", 200, 'FILLING'),
            ('FILLING', "sausage", 300, 'FILLING')
        ]
    )
    def test_get_type(self, type, name, price, expected_type):
        ingredient = Ingredient(type, name, price)

        assert ingredient.get_type()==expected_type