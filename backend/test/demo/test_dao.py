import pytest
from src.util.dao import DAO

@pytest.fixture
def dao():
    dao = DAO("user")
    dao.drop()   # starta rent

    yield dao     # ge den till testerna

    dao.drop()   # städa efter testerna

def test_valid_user_without_tasks(dao):
    user = {
        "firstName": "Anna",
        "lastName": "Andersson",
        "email": "unique1@gmail.com",
        "tasks": []
    }

    result = dao.create(user)

    assert result["firstName"] == "Anna"
    assert result["lastName"] == "Andersson"
    assert result["email"] == "unique1@gmail.com"
    assert result["tasks"] == []

def test_missing_firstName(dao):
    user = {
        "lastName": "Andersson",
        "email": "unique2@gmail.com"
    }

    with pytest.raises(Exception):
        dao.create(user)

def test_missing_lastName(dao):
    user = {
        "firstName": "Anna",
        "email": "unique3@gmail.com", 
    }

    with pytest.raises(Exception):
        dao.create(user)


def test_missing_email(dao):
    user = {
        "firstName": "Anna",
        "lastName": "Andersson"
    }

    with pytest.raises(Exception):
        dao.create(user)

def test_firstName_wrong_type(dao):
    user = {
        "firstName": 123,
        "lastName": "Andersson",
        "email": "unique4@gmail.com"
    }

    with pytest.raises(Exception):
        dao.create(user)

def test_lastName_wrong_type(dao):
    user = {
        "firstName": "Anna",
        "lastName": 123,
        "email": "unique5@gmail.com"
    }

    with pytest.raises(Exception):
        dao.create(user)

def test_email_wrong_type(dao):
    user = {
        "firstName": "Anna",
        "lastName": "Andersson",
        "email": 123
    }

    with pytest.raises(Exception):
        dao.create(user)

def test_duplicate_email(dao):
    user1 = {
        "firstName": "Anna",
        "lastName": "Andersson",
        "email": "unique6@gmail.com"
    }

    user2 = {
        "firstName": "Bob",
        "lastName": "Berg",
        "email": "unique6@gmail.com"
    }

    dao.create(user1)

    with pytest.raises(Exception):
        dao.create(user2)

def test_tasks_wrong_datatype(dao):
    user = {
        "firstName": "Anna",
        "lastName": "Andersson",
        "email": "unique7@gmail.com",
        "tasks": "wrong type"
    }

    with pytest.raises(Exception):
        dao.create(user)