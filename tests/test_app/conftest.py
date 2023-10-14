# "conftest.py" - (file name only "conftest.py" according to documentation)
# There are functions or classes, that are common for all tests, like
# connection with test_db, getting and further using user_token etc.
import json
import time

import pytest
from pytest import fixture

from app.schemas.pydantic.users.users_validation import UserValidation
from app.services.user_service import UserService
from app.services.computer_service import ComputerService, OwnersService, PhysicalService, DetailedInfoService
from app.src.generators.user_generator import FakeUser


@fixture(scope="function", autouse=True)
def remove_all_instances(started_db_session):
    UserService.del_all_instances()
    OwnersService.del_all_instances()
    PhysicalService.del_all_instances()
    DetailedInfoService.del_all_instances()
    ComputerService.del_all_instances()


@fixture(scope="function")
def get_random_users():
    users = [
        UserValidation(user_name="User1", email="user1@mail.com", phone="123456"),
        UserValidation(user_name="User2", email="user2@mail.com", phone="234567"),
        UserValidation(user_name="User3", email="user3@mail.com", phone="345678")
    ]
    return users


@fixture(scope="function")
def computers():
    computer = json.dumps({
        "status": "ACTIVE",
        "activated_at": "2013-06-01",
        "expiration_at": "2040-06-01",
        "host_v4": "91.192.222.17",
        "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
        "detailed_info": {
            "physical": {
                "color": 'green',
                "photo": 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80',
                "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
            },
            "owners": [
                {
                    "name": "Stephan Nolan",
                    "card_number": "4485835236761222",
                    "email": "shtephan.nollan@gmail.com",
                },
                {
                    "name": "Kris Nolan",
                    "card_number": "4916443741876624",
                    "email": "kris.nollan@gmail.com",
                }
            ],

        }
    })
    return computer


@fixture
def get_fake_user():
    return FakeUser()


def pytest_addoption(parser):
    parser.addoption("--browser",
                     default="chrome",
                     choices=("chrome", "firefox"))
    parser.addoption("--run_slow",
                     default="false",
                     choices=("true", "false"))


@fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.mark.skip(reason="Slow test")
def test_slow_function():
    time.sleep(3)


@pytest.mark.skipif("config.getoption('--run_slow')=='false'")
def test_slow_function():
    time.sleep(3)


def test_browser(browser):
    print(browser)
