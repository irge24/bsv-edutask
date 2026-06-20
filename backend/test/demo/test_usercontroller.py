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
    pass

def test_multiple_users_found(controller):
    pass

def test_no_user_found(controller):
    pass

def test_dao_exception(controller):
    pass