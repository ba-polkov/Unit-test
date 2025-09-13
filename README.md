# Дипломный проект. Задание 1 — Юнит-тесты

Небольшое приложение для заказа бургера и набор юнит-тестов с отчётом покрытия кода.

## Структура проекта

```
.
├── praktikum/                # код приложения
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   └── ingredient_types.py
├── tests/                    # юнит-тесты
│   ├── test_bun.py
│   ├── test_burger.py
│   └── test_database.py
├── conftest.py               # фикстуры и общая конфигурация pytest
├── pytest.ini                # базовые опции pytest + coverage, маркеры
├── praktikum.py              # пример запуска приложения (демо)
├── requirements.txt
└── README.md
```

## Требования

* Python 3.10+
* `pip` для установки зависимостей

## Установка

```bash
pip install -r requirements.txt
```

## Как устроен `pytest.ini`

Файл `pytest.ini` задаёт дефолтные опции:

* `pythonpath = .` — чтобы импорты `from praktikum...` стабильно работали из корня проекта.
* `addopts = --cov=praktikum --cov-report=term-missing --cov-report=html` — при каждом запуске `pytest`:

  * считается покрытие по пакету `praktikum`;
  * в терминал выводится список непокрытых строк;
  * генерируется HTML-отчёт в `htmlcov/`.
* Маркер `unit` зарегистрирован как «быстрые модульные тесты» — им помечены тесты.

## Запуск тестов

Запусти просто:

```bash
pytest
```

Благодаря `pytest.ini` автоматически:

* посчитается покрытие,
* появится HTML-отчёт в `htmlcov/`.

Открыть отчёт можно в браузере, файл:

```
htmlcov/index.html
```

### Запуск по маркеру

Чтобы выполнить только быстрые модульные тесты:

```bash
pytest -m unit
```