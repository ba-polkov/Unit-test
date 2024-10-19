from ya_praktikum.database import Database
from ya_praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDataBase:

    def test_available_buns(self):
        data = Database()
        available_buns = data.available_buns()

        assert available_buns[0].get_name() == "black bun"
        assert available_buns[0].get_price() == 100

    def test_available_ingredients_positive(self):
        """
        Позитивный кейс чего-то....
        Тестируется кейс, когда... Ожидается что выполняются какие-то условия
        """

        data = Database()

        # Act
        available_ingredients = data.available_ingredients()

        assert available_ingredients[0].get_name() == "hot sauce"
        assert available_ingredients[0].get_price() == 100
        assert available_ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE