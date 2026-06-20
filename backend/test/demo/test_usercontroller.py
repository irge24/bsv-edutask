import pytest
from unittest.mock import MagicMock

from src.controllers.usercontroller import UserController

@pytest.fixture
def controller():
    mocked_dao = MagicMock()
    return UserController(dao=mocked_dao)

def test_invalid_email(controller):
    incorrect_email = "hej"

    with pytest.raises(ValueError):
        controller.get_user_by_email(incorrect_email)

def test_one_user_found(controller):
    email = "hej@gmail.com"
    expected_user = {"email": email}

    controller.dao.find.return_value = [expected_user]
    result = controller.get_user_by_email(email)

    assert result == expected_user

def test_multiple_users_found(controller):
    email = "hej@gmail.com"

    user1 = {"email": email}
    user2 = {"email": email}

    controller.dao.find.return_value = [user1, user2]
    result = controller.get_user_by_email(email)

    assert result == user1

def test_no_user_found(controller):
    email = "hej@gmail.com"

    controller.dao.find.return_value = []
    result = controller.get_user_by_email(email)

    assert result is None

def test_dao_exception(controller):
    pass