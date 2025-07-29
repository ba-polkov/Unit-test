import pytest
from praktikum.bun import Bun
from praktikum.database import Database

db = Database()

class TestBun:

    def test_bun_initialization(self):
        bun = db.available_buns()[0]
        assert isinstance(bun, Bun)
        assert bun.name == "black bun"
        assert bun.price == 100

    def test_get_name(self):
        bun = db.available_buns()[1]
        assert bun.get_name() == "white bun"

    def test_get_price(self):
        bun = db.available_buns()[2]
        assert bun.get_price() == 300