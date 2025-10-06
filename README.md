## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта
├── htmlcov/  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── index.html&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- отчёт по покрытию юнит-тестами  
├── praktikum/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- пакет, содержащий код программы   
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── bun.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── burger.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── database.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── ingredient.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── ingredient_types.py  
├── src/  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── data.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- данные для параметризации  
├── tests/&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- пакет, содержащий тесты, разделенные по классам.    
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── test_bun.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── test_ingredient.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── test_database.py  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── test_burger.py  
├── praktikum.py       
├── requirements.txt  
├── pytest.ini  
└── README.md  

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

> `$ pytest --cov=praktikum --cov-report=html`
