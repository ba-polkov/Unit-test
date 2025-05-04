# conftest.py

import pytest
from bun import Bun


@pytest.fixture
def default_bun(self):
    return Bun("Краторная булка N-200i", 1255)


@pytest.fixture(params=[
    ("Флюоресцентная булка R2-D3", 988),
    ("Краторная булка N-200i", 1255)
])
def parametrized_bun(self, request):
    return Bun(*request.param)