from practicum.bun import Bun

class TestStellarBurgers:

    def test_get_name(self):
        name = 'Улетная булка'
        price = 100.5
        bun = Bun(name, price)
        actual_name = bun.get_name()
        expected_name = name

        assert actual_name == expected_name, f"Имя булки {actual_name} не соответствует ожидаемому {expected_name}"


    def test_get_price(self):
        name = 'Улетная булка'
        price = 100.5
        bun = Bun(name, price)
        actual_price = bun.get_price()
        expected_price = price

        assert actual_price == expected_price, f"Цена булки {actual_price} не соответствует ожидаемому {expected_price}"

    def test_name_is_str(self):
        name = 'Улетная булка'
        price = 100.5
        bun = Bun(name, price)
        actual_name = bun.get_name()

        assert isinstance(actual_name, str), f"Значение переменной actual_name = {actual_name} не соответствует типу str"

    def test_price_is_float_when_set_float(self):
        name = 'Улетная булка'
        price = 100.5
        bun = Bun(name, price)
        actual_price = bun.get_price()

        assert isinstance(actual_price, float), f"Значение переменной actual_price = {actual_price} не соответствует типу float"
