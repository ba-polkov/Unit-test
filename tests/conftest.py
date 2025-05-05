# conftest.py

from Diplom_1.bun import Bun
from Diplom_1.burger import Burger
from Diplom_1.ingredient import Ingredient


@pytest.fixture
def default_bun():
    """Фикстура для стандартной булки"""
    return Bun("Краторная булка N-200i", 1255)

@pytest.fixture
def empty_burger():
    """Фикстура для пустого бургера"""
    return Burger()

@pytest.fixture
def prepared_burger(default_bun):
    """Фикстура для собранного бургера (булка + 2 ингредиента)"""
    burger = Burger()
    burger.set_buns(default_bun)
    burger.add_ingredient(Ingredient("SAUCE", "Соус фирменный Space Sauce", 80))
    burger.add_ingredient(Ingredient("FILLING", "Биокотлета из марсианской Магнолии", 424))
    return burger

# Параметризованные фикстуры
@pytest.fixture(params=[
    ("Краторная булка N-200i", 1255),
    ("Флюоресцентная булка R2-D3", 988)
], ids=["krator_bun", "fluorescent_bun"])
def parametrized_bun(request):
    return Bun(*request.param)

@pytest.fixture(params=[
    ("SAUCE", "Соус фирменный Space Sauce", 80),
    ("FILLING", "Биокотлета из марсианской Магнолии", 424)
], ids=["sauce", "filling"])
def parametrized_ingredient(request):
    return Ingredient(*request.param)