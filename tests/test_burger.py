import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    @pytest.fixture
    def burger(self):
        """Фикстура для создания чистого экземпляра Burger перед каждым тестом"""
        return Burger()

    @pytest.fixture
    def mock_bun(self):
        """Фикстура для мока булочки"""
        bun = Mock()
        bun.get_price.return_value = 100
        bun.get_name.return_value = "white bun"
        return bun

    @pytest.fixture
    def mock_ingredients(self):
        """Фикстура для списка моков ингредиентов"""
        ingredient1 = Mock()
        ingredient1.get_price.return_value = 50
        ingredient1.get_name.return_value = "hot sauce"
        ingredient1.get_type.return_value = "SAUCE"

        ingredient2 = Mock()
        ingredient2.get_price.return_value = 30
        ingredient2.get_name.return_value = "cutlet"
        ingredient2.get_type.return_value = "FILLING"

        return [ingredient1, ingredient2]

    # Тесты для set_buns
    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Тесты для add_ingredient
    def test_add_ingredient(self, burger, mock_ingredients):
        burger.add_ingredient(mock_ingredients[0])
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredients[0]

    # Тесты для remove_ingredient
    def test_remove_ingredient(self, burger, mock_ingredients):
        burger.ingredients = mock_ingredients.copy()
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredients[1]

    # Тесты для move_ingredient
    @pytest.mark.parametrize(
        "initial_index,new_index,expected_order",
        [
            (0, 1, [1, 0, 2]),  # Перемещение первого элемента на вторую позицию
            (1, 0, [1, 0, 2]),  # Перемещение второго элемента на первую позицию
            (2, 1, [0, 2, 1]),  # Перемещение последнего элемента в середину
        ]
    )
    def test_move_ingredient(self, burger, initial_index, new_index, expected_order):
        # Создаем список из трех разных моков
        mock_ingredients = [Mock(), Mock(), Mock()]
        burger.ingredients = mock_ingredients.copy()

        burger.move_ingredient(initial_index, new_index)

        # Проверяем, что порядок изменился как ожидается
        assert burger.ingredients == [mock_ingredients[i] for i in expected_order]

    # Тесты для get_price
    def test_get_price_with_bun_and_ingredients(self, burger, mock_bun, mock_ingredients):
        burger.set_buns(mock_bun)
        burger.ingredients = mock_ingredients.copy()

        assert burger.get_price() == 280  # 100*2 + 50 + 30

    def test_get_price_with_only_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200  # 100*2

    def test_get_price_without_bun_should_fail(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()

    # Тесты для get_receipt
    def test_get_receipt_with_bun_and_ingredients(self, burger, mock_bun, mock_ingredients):
        burger.set_buns(mock_bun)
        burger.ingredients = mock_ingredients.copy()

        # Мокируем get_price для предсказуемого результата
        burger.get_price = Mock(return_value=350)

        expected_receipt = (
            "(==== white bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== white bun ====)\n\n"
            "Price: 350"
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_with_only_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        burger.get_price = Mock(return_value=200)

        expected_receipt = (
            "(==== white bun ====)\n"
            "(==== white bun ====)\n\n"
            "Price: 200"
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_without_bun_should_fail(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()