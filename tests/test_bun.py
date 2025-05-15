import sys

import pytest

from praktikum.bun import Bun


class TestBun:

    test_name = ['Чёрная Дырка', '', '1',
                 'Cosmic MegaBurger Bun Featuring Nanostructured Dough Matrix, '
                 'Probiotic Enrichment, and Galactic Spectrum of Vitamins',
                 '*', '{Nebula_Stars}']

    test_price = [1000, 1, 10.50, 0, -1, sys.maxsize]

    @pytest.mark.parametrize('name', test_name)
    def test_bun_name_is_set(self, name):
        bun = Bun(name, 100)

        assert bun.name == name

    @pytest.mark.parametrize('price', test_price)
    def test_bun_price_is_set(self, price):
        bun = Bun('Galaxy Bun', price)

        assert bun.price == price

    @pytest.mark.parametrize('name', test_name)
    def test_get_bun_name_return_name(self, name):
        bun = Bun(name, 100)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', test_price)
    def test_get_bun_price_return(self, price):
        bun = Bun('Galaxy Bun', price)

        assert bun.get_price() == price
