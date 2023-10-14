from jsonschema import validate
from app.src.enums.global_enums import GlobalErrorMessages
from app.schemas.pydantic.users.users_validation import UserValidation
from app.schemas.json import USER_SCHEMA


class DbResponse:

    def __init__(self, db_response):
        self.db_response = db_response

    def _response_to_dict(self):
        db_response_properties = self.db_response.__dict__
        db_response_properties.pop("id", None)
        db_response_properties.pop("_sa_instance_state", None)
        return db_response_properties

    @staticmethod
    def _json_schema_validation(instance):
        return validate(instance=instance, schema=USER_SCHEMA)

    @staticmethod
    def _pydantic_schema_validation(instance):
        properties = {attr: value for attr, value in instance.__dict__.items() if attr != "_sa_instance_state"}
        return UserValidation(**properties)

    def _get_validation_schema(self, mode="pydantic"):
        if mode == "json":
            return self._json_schema_validation
        return self._pydantic_schema_validation

    def validate_db_response(self, mode):
        schema = self._get_validation_schema(mode)
        if isinstance(self.db_response, (list, tuple)):
            for db_object in self.db_response:
                schema(db_object)
        else:
            schema(self.db_response)
        return self

    def assert_add_user(self, expected_result):
        assert self._response_to_dict() == expected_result, GlobalErrorMessages.WRONG_ADDED_USER
