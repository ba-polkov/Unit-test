import pytest

def test_bun_creation(kunzhutnaya_bun):
    assert kunzhutnaya_bun.name == "Кунжутная"
    assert kunzhutnaya_bun.price == 3.50

def test_get_name(kunzhutnaya_bun):
    assert kunzhutnaya_bun.get_name() == 'Кунжутная'

def test_get_price(kunzhutnaya_bun):
    assert kunzhutnaya_bun.get_price() == 3.50
