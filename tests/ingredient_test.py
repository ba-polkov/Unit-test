import pytest

from praktikum.ingredient import Ingredient


@pytest.fixture
def ingredient():
    return Ingredient('FILLING', 'Говяжий метеорит (отбивная)', 3000.0)

class TestIngredient:
    def test_get_type(self, ingredient):
        assert ingredient.get_type() == 'FILLING'

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == 'Говяжий метеорит (отбивная)'

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == 3000.0
