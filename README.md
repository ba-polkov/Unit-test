Дипломный проект. Задание 1: Юнит-тесты

Автотесты для проверки программы заказа бургера в Stellar Burgers

Структура проекта

QA-PYTHON-DIPLOM_1/
├── praktikum/ # Пакет с реализацией логики
│ ├── bun.py
│ ├── burger.py
│ ├── database.py
│ └── ingredient.py
│
├── tests/ # Пакет с тестами
│ ├── conftest.py
│ ├── test_bun.py
│ ├── test_burger.py
│ ├── test_database.py
│ └── test_ingredient.py
│
├── data.py # Тестовые данные
├── requirements.txt
└── README.md


Тестовое покрытие

Покрытие 100% (отчёт в `htmlcov/index.html`)

| Класс | Тесты |
|-----------------|-----------------------------------------------------------------------------------------|
| `test_bun.py` | `test_get_name`, `test_get_price`, `test_invalid_price_raises_error` |
| `test_burger.py`| `test_set_buns`, `test_add_ingredient`, `test_remove_ingredient`,`test_move_ingredient`, `test_get_price`, `test_get_receipt` |
| `test_database.py`| `test_available_buns`, `test_available_ingredients` |
| `test_ingredient.py`| `test_get_type`, `test_get_price`, `test_get_name`, `test_invalid_type_raises_error` |

Установка и запуск

1. Установка зависимостей

pip3 install -r requirements.txt

2. Запуск всех тестов с генерацией отчёта о покрытии

pytest --cov=praktikum --cov-report=html

3. Просмотр отчёта

Откройте файл htmlcov/index.html в браузере.

Особенности реализации

Фикстуры вынесены в conftest.py

Использованы моки для изоляции тестов

Параметризация для проверки разных сценариев

Проверка обработки ошибок для невалидных данных