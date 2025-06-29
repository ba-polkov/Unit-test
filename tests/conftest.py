import pytest
from faker import Faker

from praktikum.bun import Bun

fake = Faker("ru_RU")


@pytest.fixture
def create_bun():
    name = fake.word()
    price = round(fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1.0, max_value=100.0), 2)
    return Bun(name=name, price=price)
