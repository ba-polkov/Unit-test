import unittest
import pytest
from ..praktikum.bun import Bun


@pytest.mark.parametrize("name, price, expected_name, expected_price", [
    ("black bun", 100, "black bun", 100),
    ("white bun", 200, "white bun", 200),
    ("red bun", 300, "red bun", 300)
])
def test_bun(name, price, expected_name, expected_price):
    bun = Bun(name, price)
    assert bun.get_name() == expected_name
    assert bun.get_price() == expected_price


class TestBun(unittest.TestCase):

    def setUp(self):
        self.bun = Bun("black bun", 100)

    def test_get_name(self):
        self.assertEqual(self.bun.get_name(), "black bun")

    def test_get_price(self):
        self.assertEqual(self.bun.get_price(), 100)

if __name__ == '__main__':
    unittest.main()
