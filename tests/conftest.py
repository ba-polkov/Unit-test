import pytest
from praktikum.bun import Bun


#Создаем тестовую булку
@pytest.fixture
def cheese_bun():
    return Bun(name="Сырная булка", price=99)





