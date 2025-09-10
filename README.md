## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта
Diplom_1/
├── conftest.py
├── data/
│   ├── fooditems.py
├── praktikum/
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   ├── ingredient_types.py
│   ├── __init__.py
├── praktikum.py
├── README.md
├── requirements.txt
├── tests/
│   ├── test_bun.py - Содержит тесты для класса Булочка (Bun):
│   ├── test_burger.py - Включает тесты для класса Бургер (Burger)
│   ├── test_database.py - Тестирует работу с базой данных
│   ├── test_ingridient.py - Содержит тесты для класса Ингредиент (Ingredient)
│   ├── __init__.py




- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`

Автор: Артеев Дмитрий, 26-я когорта