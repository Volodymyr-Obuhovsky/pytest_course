import pytest
from app.services.user_service import UserService
from app.src.enums.global_enums import GlobalErrorMessages
from app.src.baseclasses.baseclasses import DbResponse


@pytest.mark.development
@pytest.mark.usefixtures("remove_all_instances")
class TestApp:
    # TestApp is an example a group tests and fixtures
    # it is a function, that will be executed before your testcase or
    # may be used like local valuable in function block code

    def test_users_quantity(self, get_random_users):
        # Test special "UserService" method ".users_quantity()"
        # 1. Inside fixture "remove_all_users" implicitly will be executed fixture "started_db_session",
        #    after that, will be cleaned db table "users" by self "remove_all_users"
        # 2. Via fixture "get_random_users", we will get list random users and inside loop "for...in..."
        #    add each user from this list to database
        # 3. Get users quantity by special method ".users_quantity()" and put in variable "result"
        # 4. Compare "result" with "expected_result"
        for user in get_random_users:
            UserService.create_instance(user)

        result = UserService.get_instances_quantity()
        expected_result = len(get_random_users)
        assert result == expected_result, GlobalErrorMessages.WRONG_USER_QUANTITY

    def test_add_user(self, get_random_users):
        added_user = get_random_users[0]
        UserService.create_instance(added_user)
        expected_result = get_random_users[0].model_to_dict()
        DbResponse(added_user).validate_db_response(mode="pydantic").assert_add_user(expected_result)

    def test_delete_user(self, get_random_users):
        # Test special "UserService" method ".delete_user()"
        # 1. Inside fixture "remove_all_users" implicitly will be executed fixture "started_db_session",
        #    after that, will be cleaned db table "users" by self "remove_all_users"
        # 2. Via special method ".add_user()" we add first user from users list (fixture - "get_random_users"),
        #    and get user id from ".add_user()"
        # 3. Remove this user from db via special method ".delete_user()"
        # 4. Compare quantity users in db with expected result - 0 users
        user_id = UserService.create_instance(get_random_users[0])
        UserService.del_instance(user_id)
        result = UserService.get_instances_quantity()
        assert result == 0, GlobalErrorMessages.WRONG_DELETE_USER
