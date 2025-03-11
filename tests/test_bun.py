import pytest
from bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price, expected_name, expected_price",
    [
        ("Флюоресцентная булка R2-D3", 988, "Флюоресцентная булка R2-D3", 988,),
        ("Краторная булка N-200i", 1255, "Краторная булка N-200i", 1255),
    ])
    def test_bun(
            self,
            name,
            price,
            expected_name,
            expected_price
    ):
        bun = Bun(name, price)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price