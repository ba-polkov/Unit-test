##Ссылки на GitHub

Задание 1: https://github.com/Yandex-Practicum/qa-python-diplom/pull/259

Задание 2: https://github.com/probyfalcon-s/Diplom_2

Задание 3: https://github.com/probyfalcon-s/Diplom_3
Комментарий для ревьюера

Здесь можно написать пояснения к своей работе

## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам. Например, `bun_test.py`, `burger_test.py` и т.д.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`
