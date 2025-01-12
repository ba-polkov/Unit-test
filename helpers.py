import random
from faker import Faker
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class RandomCred:
    def generate_random_float():
        return  random.uniform(0.0, 999.99)

    def generate_random_name():
        fake = Faker()
        name = fake.name()
        return name

    def random_choice_ingredients():
        types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
        random_type = random.choice(types)
        return random_type