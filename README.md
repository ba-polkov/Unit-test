## Дипломный проект. Задание 1: Юнит-тесты
## Студент Фронтова Анастасия 
## Кагорта 22

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `test_bun.py`, `test_burger.py`, `test_database.py`, `test_ingredient.py`
- conftest.py - файл с фикстурами
- praktikum.py

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ python -m pytest --cov=praktikum --cov-report=html`
