from praktikum.bun import Bun

def test_bun_mock_get_name(bun_mock):
    assert bun_mock.get_name() == bun_mock._expected_name

def test_bun_mock_get_price():
    bun = Bun("test bun", 123)
    assert bun.get_name() == "test bun" and bun.get_price() == 123