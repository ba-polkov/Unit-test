import pytest


class TestBurger:
    # Проверяем, что новый бургер создаётся без булки
    def test_burger_init_no_buns_in_new(self, burger):
        assert burger.bun is None

    # Проверяем, что список ингредиентов пуст при создании нового бургера
    def test_burger_init_no_ingredients_in_new(self, burger):
        assert burger.ingredients == []

    # Проверяем, что метод set_buns корректно сохраняет объект булки в атрибуте bun
    def test_set_bun_added_to_burger(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверяем, что метод add_ingredient добавляет ингредиент в список burger.ingredients
    def test_add_ingredient_added_to_burger(self, burger, mock_filling):
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling

    # Проверяем, что метод remove_ingredient удаляет ингредиент из списка burger.ingredients
    def test_remove_ingredient_deleted_from_burger(self, burger, mock_filling):
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0
        assert mock_filling not in burger.ingredients

    # Проверяем, что метод move_ingredient перемещает ингредиенты внутри списка burger.ingredients
    def test_move_ingredient_replaced_ingredient(
        self, burger, mock_filling, mock_sause
    ):
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sause)
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0].get_name() == mock_sause.get_name()
        assert burger.ingredients[1].get_name() == mock_filling.get_name()

    # Проверяем, что метод get_price рассчитывает итоговую стоимость бургера корректно
    @pytest.mark.parametrize(
        "ingredients",
        [
            [],  # только булка
            ["filling"],  # булка + начинка
            ["sause"],  # булка + соус
            ["filling", "sause"],  # булка + начинка + соус
        ],
    )
    def test_get_price_of_burger(
        self, burger, mock_bun, mock_filling, mock_sause, ingredients
    ):
        burger.set_buns(mock_bun)

        if "filling" in ingredients:
            burger.add_ingredient(mock_filling)
        if "sause" in ingredients:
            burger.add_ingredient(mock_sause)

        expected_price = mock_bun.get_price.return_value * 2
        if "filling" in ingredients:
            expected_price += mock_filling.get_price.return_value
        if "sause" in ingredients:
            expected_price += mock_sause.get_price.return_value

        actual_price = burger.get_price()

        assert actual_price == expected_price

    # Проверяем, что метод get_receipt выводит чек со всеми элементами бургера и стоимостью корректно
    @pytest.mark.parametrize(
        "ingredients",
        [
            [],  # только булка
            ["filling"],  # булка + начинка
            ["sause"],  # булка + соус
            ["filling", "sause"],  # булка + начинка + соус
        ],
    )
    def test_get_receipt_with_ingredients(
        self, burger, mock_bun, mock_filling, mock_sause, ingredients
    ):
        burger.set_buns(mock_bun)

        if "filling" in ingredients:
            burger.add_ingredient(mock_filling)
        if "sause" in ingredients:
            burger.add_ingredient(mock_sause)

        receipt_part = [f"(==== {mock_bun.get_name()} ====)"]
        if "filling" in ingredients:
            receipt_part.append(
                f"= {str(mock_filling.get_type()).lower()} {mock_filling.get_name()} ="
            )
        if "sause" in ingredients:
            receipt_part.append(
                f"= {str(mock_sause.get_type()).lower()} {mock_sause.get_name()} ="
            )
        receipt_part.append(f"(==== {mock_bun.get_name()} ====)\n")
        receipt_part.append(f"Price: {burger.get_price()}")
        expected_receipt = "\n".join(receipt_part)

        actual_receipt = burger.get_receipt()

        assert actual_receipt == expected_receipt
