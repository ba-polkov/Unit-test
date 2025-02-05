import pytest
from praktikum.database import Database

@pytest.fixture(scope="session")
def database_instance():
    return Database()