from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_init_creates_buns_list_of_length_3(self):
        db = Database()
        assert len(db.buns) == 3, \
            f"Ожидалось 3 булочки, получено {len(db.buns)}"

    def test_database_init_creates_ingredients_list_of_length_4(self):
        db = Database()
        assert len(db.ingredients) == 6, \
            f"Ожидалось 4 ингредиента, получено {len(db.ingredients)}"

    def test_available_buns_returns_list_of_length_3(self):
        db = Database()
        assert len(db.available_buns()) == 3, \
            f"Ожидалось 3 булочки, получено {len(db.available_buns())}"

    def test_available_ingredients_returns_list_of_length_4(self):
        db = Database()
        assert len(db.available_ingredients()) == 6, \
            f"Ожидалось 4 ингредиента, получено {len(db.available_ingredients())}"

    # Проверка булок
    def test_first_bun_has_name_black_bun(self):
        db = Database()
        assert db.buns[0].get_name() == "black bun", \
            f"Ожидалось имя булочки 'black bun', получено '{db.buns[0].get_name()}'"

    def test_first_bun_has_price_100(self):
        db = Database()
        assert db.buns[0].get_price() == 100, \
            f"Ожидалась цена булочки '100', получена '{bun.price}'"

    def test_second_bun_has_name_white_bun(self):
        db = Database()
        assert db.buns[1].get_name() == "white bun", \
            f"Ожидалось имя булочки 'white bun', получено '{bun.name}'"

    def test_second_bun_has_price_200(self):
        db = Database()
        assert db.buns[1].get_price() == 200, \
            f"Ожидалась цена булочки '200', получена '{bun.price}'"

    def test_third_bun_has_name_red_bun(self):
        db = Database()
        assert db.buns[2].get_name() == "red bun", \
            f"Ожидалось имя булочки 'red bun', получено '{bun.name}'"

    def test_third_bun_has_price_300(self):
        db = Database()
        assert db.buns[2].get_price() == 300, \
            f"Ожидалась цена булочки '300', получена '{bun.price}'"

    # Проверка ингредиентов
    # Соусы
    def test_first_ingredient_has_type_sauce(self):
        db = Database()
        assert db.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE, \
            f"Ожидался тип ингредиента '{INGREDIENT_TYPE_SAUCE}', получен '{db.ingredients[0].get_type()}'"

    def test_first_ingredient_has_name_hot_sauce(self):
        db = Database()
        assert db.ingredients[0].get_name() == "hot sauce", \
            f"Ожидалось название ингредиента 'hot sauce', получено '{db.ingredients[0].get_name()}'"

    def test_first_ingredient_has_price_100(self):
        db = Database()
        assert db.ingredients[0].get_price() == 100, \
            f"Ожидалась цена ингредиента '100', получена '{db.ingredients[0].get_price()}'"

    def test_second_ingredient_has_type_sauce(self):
        db = Database()
        assert db.ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE, \
            f"Ожидался тип ингредиента '{INGREDIENT_TYPE_SAUCE}', получен '{db.ingredients[1].get_type()}'"

    def test_second_ingredient_has_name_sour_cream(self):
        db = Database()
        assert db.ingredients[1].get_name() == "sour cream", \
            f"Ожидалось название ингредиента 'sour cream', получено '{db.ingredients[1].get_name()}'"

    def test_second_ingredient_has_price_200(self):
        db = Database()
        assert db.ingredients[1].get_price() == 200, \
            f"Ожидалась цена ингредиента '200', получена '{db.ingredients[1].get_price()}'"

    def test_third_ingredient_has_type_sauce(self):
        db = Database()
        assert db.ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE, \
            f"Ожидался тип ингредиента '{INGREDIENT_TYPE_SAUCE}', получен '{db.ingredients[2].get_type()}'"

    def test_third_ingredient_has_name_chili_sauce(self):
        db = Database()
        assert db.ingredients[2].get_name() == "chili sauce", \
            f"Ожидалось название ингредиента 'chili sauce', получено '{db.ingredients[2].get_name()}'"

    def test_third_ingredient_has_price_300(self):
        db = Database()
        assert db.ingredients[2].get_price() == 300, \
            f"Ожидалась цена ингредиента '300', получена '{db.ingredients[2].get_price()}'"

    # Начинки
    def test_fourth_ingredient_has_type_filling(self):
        db = Database()
        assert db.ingredients[3].get_type() == INGREDIENT_TYPE_FILLING, \
            f"Ожидался тип ингредиента '{INGREDIENT_TYPE_FILLING}', получен '{db.ingredients[3].get_type()}'"

    def test_fourth_ingredient_has_name_cutlet(self):
        db = Database()
        assert db.ingredients[3].get_name() == "cutlet", \
            f"Ожидалось название ингредиента 'cutlet', получено '{db.ingredients[3].get_name()}'"

    def test_fourth_ingredient_has_price_100(self):
        db = Database()
        assert db.ingredients[3].get_price() == 100, \
            f"Ожидалась цена ингредиента '100', получена '{db.ingredients[3].get_price()}'"

    def test_fifth_ingredient_has_type_filling(self):
        db = Database()
        assert db.ingredients[4].get_type() == INGREDIENT_TYPE_FILLING, \
            f"Ожидался тип ингредиента '{INGREDIENT_TYPE_FILLING}', получен '{db.ingredients[4].get_type()}'"

    def test_fifth_ingredient_has_name_dinosaur(self):
        db = Database()
        assert db.ingredients[4].get_name() == "dinosaur", \
            f"Ожидалось название ингредиента 'dinosaur', получено '{db.ingredients[4].get_name()}'"

    def test_fifth_ingredient_has_price_200(self):
        db = Database()
        assert db.ingredients[4].get_price() == 200, \
            f"Ожидалась цена ингредиента '200', получена '{db.ingredients[4].get_price()}'"

    def test_sixth_ingredient_has_type_filling(self):
        db = Database()
        assert db.ingredients[5].get_type() == INGREDIENT_TYPE_FILLING, \
            f"Ожидался тип ингредиента '{INGREDIENT_TYPE_FILLING}', получен '{db.ingredients[5].get_type()}'"

    def test_sixth_ingredient_has_name_sausage(self):
        db = Database()
        assert db.ingredients[5].get_name() == "sausage", \
            f"Ожидалось название ингредиента 'sausage', получено '{db.ingredients[5].get_name()}'"

    def test_sixth_ingredient_has_price_300(self):
        db = Database()
        assert db.ingredients[5].get_price() == 300, \
            f"Ожидалась цена ингредиента '300', получена '{db.ingredients[5].get_price()}'"

