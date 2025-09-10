import pytest

from data.fooditems import ingredients
from praktikum.ingredient import Ingredient


class TestIngredient:
    """
    Класс для тестирования функциональности класса Ingredient.

    Содержит тесты для проверки корректности работы основных методов.
    """

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        ingredients,
        ids=[f"{name} ({price} руб.)" for _, name, price in ingredients]
    )
    def test_ingredient_get_price(
        self,
        ingredient_type: str,
        name: str,
        price: float
    ) -> None:
        """
        Тест проверки корректности получения цены ингредиента.

        :param ingredient_type: Тип ингредиента (sauce/main)
        :param name: Название ингредиента
        :param price: Ожидаемая цена ингредиента
        """
        # Создаем экземпляр ингредиента
        ingredient = Ingredient(ingredient_type, name, price)

        # Проверяем соответствие полученной цены ожидаемой
        assert ingredient.get_price() == price, (
            f"Неверная цена ингредиента: {price}"
        )

        # Проверяем тип возвращаемого значения
        assert isinstance(ingredient.get_price(), (int, float)), (
            "Цена должна быть числом"
        )

        # Проверяем положительность цены
        assert ingredient.get_price() > 0, "Цена не может быть отрицательной"

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        ingredients,
        ids=[f"{name} ({price} руб.)" for _, name, price in ingredients]
    )
    def test_ingredient_get_name(
        self,
        ingredient_type: str,
        name: str,
        price: float
    ) -> None:
        """
        Тест проверки корректности получения названия ингредиента.

        :param ingredient_type: Тип ингредиента (sauce/main)
        :param name: Ожидаемое название ингредиента
        :param price: Цена ингредиента
        """
        # Создаем экземпляр ингредиента
        ingredient = Ingredient(ingredient_type, name, price)

        # Проверяем соответствие полученного названия ожидаемому
        assert ingredient.get_name() == name, (
            f"Неверное название ингредиента: {name}"
        )

        # Проверяем тип возвращаемого значения
        assert isinstance(ingredient.get_name(), str), (
            "Название должно быть строкой"
        )

    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        ingredients,
        ids=[f"{name} ({price} руб.)" for _, name, price in ingredients]
    )
    def test_ingredient_get_type(
        self,
        ingredient_type: str,
        name: str,
        price: float
    ) -> None:
        """
        Тест проверки корректности получения типа ингредиента.

        :param ingredient_type: Ожидаемый тип ингредиента (sauce/main)
        :param name: Название ингредиента
        :param price: Цена ингредиента
        """
        # Создаем экземпляр ингредиента
        ingredient = Ingredient(ingredient_type, name, price)

        # Проверяем соответствие полученного типа ожидаемому
        assert ingredient.get_type() == ingredient_type, (
            f"Неверный тип ингредиента: {ingredient_type}"
        )
