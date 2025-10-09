Задание 1 Юнит-тесты

Косач Евгений 29-я когорта

Diplom/
├── .gitignore
├── requirements.txt
├── praktikum/
│   ├── __init__.py
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   ├── ingredient_types.py
│   └── praktikum.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    └── test_burger.py

    # Установка зависимостей
pip install -r requirements.txt

# Запуск тестов с проверкой покрытия
pytest --cov=praktikum --cov-report=html