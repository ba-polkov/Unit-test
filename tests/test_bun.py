import random

from praktikum.bun import Bun
from data_for_tests import constants as const


class TestBun:

    def test_get_name(self):
        bun_name = random.choice(const.bun_names)
        bun = Bun(bun_name, random.randint(const.min_bun_price, const.max_bun_price))
        assert bun.get_name() == bun_name

    def test_get_price(self):
        test_price = random.uniform(const.min_bun_price, const.max_bun_price)
        bun = Bun(random.choice(const.bun_names), test_price)
        assert bun.get_price() == test_price