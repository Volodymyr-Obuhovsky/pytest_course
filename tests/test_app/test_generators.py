import pytest


@pytest.mark.development
class TestFakeUser:

    @pytest.mark.parametrize("attribute", [
        "user_name",
        "password",
        "phone",
        "address"
    ])
    def test_delete_user_property(self, attribute, get_fake_user):
        user = get_fake_user.create()
        del user[attribute]
        assert not hasattr(user, attribute)

    def test_update_inner_property(self, get_fake_user):
        user = get_fake_user
        user.update_inner_property(
            inner_structure=["work_history", "companies", "position"],
            attribute="position",
            value="developer"
        )
        print(user.properties)
        expected_result = "developer"
        result = user.properties["work_history"]["companies"]["position"]
        assert result == expected_result
