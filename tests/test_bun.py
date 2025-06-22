from praktikum.bun import Bun

def test_bun_get_name():
    bun = Bun("black bun", 100)
    assert bun.get_name() == "black bun"

def test_bun_get_price():
    bun = Bun("white bun", 250)
    assert bun.get_price() == 250
