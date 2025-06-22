import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("Юпитер", "сто рублей"),
            ("Орбита", 200.5),
            ("Марс", 0),
            ("", 10),  # Пустое имя
            ("very long bun name" * 10, 999.99),  # Длинное имя
            ("@рбита", 99), #Имя со спецсимволом
        ],
    )
    def test_bun_initialization(self, name, price):
        """Проверяем, что булочка корректно инициализируется с разными именами и ценами."""
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_name_is_string(self):
        """Проверяем, что имя булочки - строка."""
        bun = Bun("test bun", 100)
        assert isinstance(bun.get_name(), str)

    @pytest.mark.parametrize(
        "price, expected_type",
        [
            (100, float),  # По аннотации должен возвращать float
            (100.5, float),  # Очевидный float
            (0, float),  # Ноль тоже должен быть float
            (-50, float),  # Отрицательные числа
            (1e10, float)  # Большие числа
        ],
        ids=[
            "integer_should_be_float",
            "float_unchanged",
            "zero",
            "negative",
            "large_number"
        ]
    )
    def test_get_price_returns_float(self, price, expected_type):
        """
        Проверяем что get_price() возвращает значения правильного типа.
        По аннотации метода должен возвращать float, но текущая реализация
        возвращает int для целых чисел - это ошибка.
        """
        bun = Bun("test bun", price)
        actual_type = type(bun.get_price())

        # Проверяем соответствие документации
        if expected_type != actual_type:
            pytest.fail(
                f"По аннотации метод должен возвращать {expected_type}, "
                f"но вернул {actual_type} для значения {price}. "
                "Это нарушение контракта метода."
            )

        # Дополнительная проверка, что значение сохраняется
        assert bun.get_price() == price

    def test_get_price_type_annotation(self):
        """Проверяем, что аннотация типа метода get_price() соответствует float."""
        from inspect import signature
        sig = signature(Bun.get_price)
        assert sig.return_annotation is float, "Аннотация типа должна быть float"
