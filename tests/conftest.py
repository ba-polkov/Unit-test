# conftest.py

import pytest
from bun import Bun


@pytest.fixture
def default_bun():
    return Bun("Краторная булка N-200i", 1255)


@pytest.fixture(params=[
    ("Флюоресцентная булка R2-D3", 988),
    ("Краторная булка N-200i", 1255)
])
def parametrized_bun(request):
    return Bun(*request.param)