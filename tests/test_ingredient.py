import pytest  # Добавляем импорт pytest
import allure

class TestIngredient:
    @allure.title('Получение типа ингредиента')
    @pytest.mark.parametrize('ingredient_type', ['sauce', 'filling'])
    def test_get_type(self, ingredient_type, request, ingredient_data):
        mock_ingredient = request.getfixturevalue(f'mock_{ingredient_type}')
        assert mock_ingredient.get_type() == ingredient_data[ingredient_type]['type']

    @allure.title('Получение названия ингредиента')
    @pytest.mark.parametrize('ingredient_type', ['sauce', 'filling'])
    def test_get_name(self, ingredient_type, request, ingredient_data):
        mock_ingredient = request.getfixturevalue(f'mock_{ingredient_type}')
        assert mock_ingredient.get_name() == ingredient_data[ingredient_type]['name']

    @allure.title('Получение цены ингредиента')
    @pytest.mark.parametrize('ingredient_type', ['sauce', 'filling'])
    def test_get_price(self, ingredient_type, request, ingredient_data):
        mock_ingredient = request.getfixturevalue(f'mock_{ingredient_type}')
        assert mock_ingredient.get_price() == ingredient_data[ingredient_type]['price']