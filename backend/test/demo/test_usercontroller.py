import pytest
from unittest.mock import MagicMock

from src.controllers.usercontroller import UserController

@pytest.fixture
def controller():
    mocked_dao = MagicMock()
    return UserController(dao=mocked_dao)

def test_invalid_email(controller):
    pass

def test_one_user_found(controller):
    pass


def test_multiple_users_found(controller):
    pass


def test_no_user_found(controller):
    pass


def test_dao_exception(controller):
    pass