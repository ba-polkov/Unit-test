import pytest
from unittest.mock import Mock
import sys
import os

# Добавляем корень проекта в пути поиска Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from praktikum.bun import Bun

class TestBun:
    """Тест-кейсы для класса Bun (булочка для бургера)"""
    
    # Тест-кейс 1: Проверка создания булочки с корректными параметрами
    def test_create_bun_with_valid_parameters(self):
        bun = Bun("Краторная булка", 100)
        assert bun.get_name() == "Краторная булка"
    
    # Тест-кейс 2: Проверка получения цены булочки
    def test_get_bun_price(self):
        bun = Bun("Белая булка", 200)
        assert bun.get_price() == 200
    
    # Тест-кейс 3: Проверка строкового представления булочки
    def test_bun_string_representation(self):
        bun = Bun("Чёрная булка", 300)
        assert str(bun) == "Булочка: Чёрная булка"
    
    # Тест-кейс 4: Проверка создания булочки с нулевой ценой
    def test_create_bun_with_zero_price(self):
        bun = Bun("Булка", 0)
        assert bun.get_price() == 0
    
    # Тест-кейс 5: Проверка создания булочки с минимальной ценой
    def test_create_bun_with_minimal_price(self):
        bun = Bun("Булка", 1)
        assert bun.get_price() == 1
    
    # Тест-кейс 6: Проверка создания булочки с большой ценой
    def test_create_bun_with_large_price(self):
        bun = Bun("Булка", 999999)
        assert bun.get_price() == 999999
    
    # Тест-кейс 7: Проверка вызова исключения при пустом имени
    def test_create_bun_with_empty_name_raises_exception(self):
        with pytest.raises(ValueError, match="Имя не может быть пустым"):
            Bun("", 100)
    
    # Тест-кейс 8: Проверка вызова исключения при None в имени
    def test_create_bun_with_none_name_raises_exception(self):
        with pytest.raises(TypeError, match="Имя должно быть строкой"):
            Bun(None, 100)
    
    # Тест-кейс 9: Проверка вызова исключения при отрицательной цене
    def test_create_bun_with_negative_price_raises_exception(self):
        with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
            Bun("Булка", -100)
    
    # Тест-кейс 10: Проверка работы с mock-объектом
    def test_mock_bun_behavior(self):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_name.return_value = "Маковая булка"
        mock_bun.get_price.return_value = 250
        assert mock_bun.get_name() == "Маковая булка"
        assert mock_bun.get_price() == 250