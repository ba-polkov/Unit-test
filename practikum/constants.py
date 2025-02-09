from practikum.bun import Bun
from practikum.ingredient import Ingredient
from practikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


#данные для Bun
H_BUNS = [                      #тестовые данные для параметризации Bun
    ("Plasma Bun", 25.0),
    ("Ice Bun", 10.0)
]



#данные для Ingredients
H_NAME_FILLING = "test filling"     #тестовое имя для наполнителя
H_PRICE_FILLING = 50.0              #тестовая цена для наполнителя

H_NAME_SAUSE = "test sauce"         #тестовое имя для соуса
H_PRICE_SAUSE = 100.0               #тестовая цена для соуса

H_INGREDIENTS = [                    #тестовые данные для параметризации ингредиентов
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 40.0),
    (INGREDIENT_TYPE_FILLING, "onion", 15.0),
    (INGREDIENT_TYPE_SAUCE, "ketchup", 20.0),
    (INGREDIENT_TYPE_FILLING, "cheese", 35.0)]





#данные для Database
#данные, которые содержатся в исходной Database
H_DB_BUNS = [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
        ]
#данные, которые содержатся в исходной Database
H_DB_INGREDIENTS = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),

    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]
#Мок данные для теста Database
H_DB =[
    ([Bun("rise bun", 50),
      Bun("rye bun", 75)],
     [Ingredient(INGREDIENT_TYPE_SAUCE, "cheese sauce", 30.0),
      Ingredient(INGREDIENT_TYPE_FILLING, "mayo", 20.0)]
     ),
    (
        [Bun("red bun", 350)], #мокированные данные, одноименные с исходными
        [Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", 25.0)]
    )
    ]
