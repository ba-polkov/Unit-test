import pytest


class TestBun:

    def test_bun(self, bun):
        assert bun.get_name() == bun.name
        assert bun.get_price() == bun.price
