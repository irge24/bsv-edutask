import pytest
from src.util.dao import DAO

@pytest.fixture
def dao():
    dao = DAO("user")
    dao.drop()   # starta rent

    yield dao     # ge den till testerna

    dao.drop()   # städa efter testerna