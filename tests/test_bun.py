import pytest
from praktikum.bun import Bun


class TestBun:

    def test_get_name(self, default_bun):
        assert default_bun.get_name() == "Стандартная булочка", "Название булочки не соответствует ожидаемому"

    def test_get_price(self, default_bun):
        assert default_bun.get_price() == 1.0, "Цена булочки не соответствует ожидаемой"


@pytest.mark.parametrize("name, price", [
    ("Булочка с кунжутом", 1.2),
    ("Булочка без глютена", 1.5),
    ("Бриошь", 1.8),
    ("Цельнозерновая булочка", 1.3),
])
def test_bun_parameters(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name, f"Название булочки должно быть '{name}'"
    assert bun.get_price() == price, f"Цена булочки должна быть '{price}'"
