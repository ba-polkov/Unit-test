import pytest
from unittest.mock import Mock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    @pytest.fixture
    def real_buns(self):
        return [
            Bun("black bun", 100),
            Bun("white bun", 200),
            Bun("red bun", 300)
        ]

    @pytest.fixture
    def real_ingredients(self):
        return [
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]

    def test_initial_state(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_integration_with_mocks(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "hot sauce"
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "cutlet"

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        assert burger.bun.get_name() == "black bun"
        assert burger.ingredients[0].get_name() == "hot sauce"
        assert burger.ingredients[1].get_name() == "cutlet"

    def test_get_price(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == 250  # 100*2 + 50

    def test_ingredient_types(self):
        burger = Burger()
        mock_sauce = Mock()
        mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_filling = Mock()
        mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert burger.ingredients[1].get_type() == INGREDIENT_TYPE_FILLING

    def test_receipt_format(self):
        burger = Burger()

        # Создаем мок булочки с реализацией get_price()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "white bun"
        mock_bun.get_price.return_value = 200  # Добавляем возвращаемое значение для цены

        # Создаем моки ингредиентов
        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient1.get_name.return_value = "sour cream"
        mock_ingredient1.get_price.return_value = 100  # Цена соуса

        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient2.get_name.return_value = "dinosaur"
        mock_ingredient2.get_price.return_value = 150  # Цена начинки

        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        # Мокаем метод get_price() для бургера
        with patch.object(burger, 'get_price', return_value=600):  # 200*2 + 100 + 150 = 650
            receipt = burger.get_receipt()
            lines = receipt.split('\n')

            assert "(==== white bun ====)" in lines[0]
            assert "= sauce sour cream =" in lines[1]
            assert "= filling dinosaur =" in lines[2]
            assert "(==== white bun ====)" in lines[3]
            assert "Price: 600" in lines[5]  # Проверяем ожидаемую цену

    def test_move_ingredient_same_index(self):
        """Проверка перемещения ингредиента на тот же индекс"""
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        # Проверяем, что метод не ломается при new_index == index
        burger.move_ingredient(0, 0)
        assert burger.ingredients == [mock_ingredient]  # Состав не изменился

    def test_get_receipt_price_formatting(self):
        """Проверка точного форматирования цены в чеке"""
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = "test bun"
        burger.set_buns(mock_bun)

        # Мокаем get_price(), чтобы вернуть фиксированное значение
        with patch.object(burger, 'get_price', return_value=123.45):
            receipt = burger.get_receipt()
            assert "Price: 123.45" in receipt  # Проверяем точный формат

    def test_get_receipt_with_no_bun_raises_error(self):
        """Проверка, что get_receipt() падает, если булочка не установлена"""
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()  # Должен упасть, так как bun=None

    def test_remove_ingredient_from_empty_burger(self):
        """Попытка удаления из пустого бургера должна вызывать IndexError"""
        burger = Burger()
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient_invalid_index(self):
        """Попытка перемещения несуществующего ингредиента"""
        burger = Burger()
        with pytest.raises(IndexError):
            burger.move_ingredient(0, 1)  # Нет ингредиентов!