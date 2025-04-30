from praktikum.bun import Bun

def test_bun_creation():
    bun = Bun("Brioche", 1.75)
    assert bun.get_name() == "Brioche"
    assert bun.get_price() == 1.75
