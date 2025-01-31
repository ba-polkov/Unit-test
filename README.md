## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100%, [отчет](htmlcov/index.html)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

``` shell
    pip install -r requirements.txt
```

**Запуск автотестов и создание [HTML-отчета](htmlcov/index.html) о покрытии**

``` shell
    pytest --cov=praktikum --cov-report=html --alluredir=allure_results
``` 

**Посмотреть отчет allure**

``` shell
    allure serve allure_results
``` 

