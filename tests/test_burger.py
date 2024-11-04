
def test_set_bun(bun, burger_with_bun):
    assert burger_with_bun.bun == bun


def test_add_ingredient(burger_with_bun, ingredient):
    burger_with_bun.add_ingredient(ingredient)
    assert len(burger_with_bun.ingredients) == 1
    assert burger_with_bun.ingredients[0] == ingredient


def test_remove_ingredient(burger_with_bun, ingredient):
    burger_with_bun.add_ingredient(ingredient)
    burger_with_bun.remove_ingredient(0)
    assert len(burger_with_bun.ingredients) == 0


def test_move_ingredient(burger_with_bun, ingredient, ingredient2):
    burger_with_bun.add_ingredient(ingredient)
    burger_with_bun.add_ingredient(ingredient2)

    burger_with_bun.move_ingredient(0, 1)
    assert burger_with_bun.ingredients[0] == ingredient2
    assert burger_with_bun.ingredients[1] == ingredient


def test_get_price(burger_with_bun, ingredient):
    burger_with_bun.add_ingredient(ingredient)
    price = burger_with_bun.get_price()
    assert price == 51


def test_get_receipt(burger_with_bun, ingredient):
    burger_with_bun.add_ingredient(ingredient)
    expected_receipt = (
        "(==== White Bun ====)\n"
        "= topping lettuce =\n"
        "(==== White Bun ====)\n"
        "Price: 51"
    )
    assert burger_with_bun.get_receipt() == expected_receipt
