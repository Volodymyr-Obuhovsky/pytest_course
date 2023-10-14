import json

from app.exceptions import InsertError, ValidDataError
from app.models import Computer, Owners, DetailedInfo, Physical, DbTables
from app.crud.crud import ComputerQuery, OwnersQuery, DetailedInfoQuery, PhysicalQuery
from app.conect_with_db import Base, engine, db_context
from app.services.base_service import BaseService
from app.schemas.pydantic.computers.computer_validation import ComputerValidation

Base.metadata.create_all(bind=engine)


class OwnersService(BaseService):
    DB_TABLE = Owners
    DB_TABLE_QUERY = OwnersQuery


class PhysicalService(BaseService):
    DB_TABLE = Physical
    DB_TABLE_QUERY = PhysicalQuery


class DetailedInfoService(BaseService):
    DB_TABLE = DetailedInfo
    DB_TABLE_QUERY = DetailedInfoQuery


class ComputerService(BaseService):
    DB_TABLE = Computer
    DB_TABLE_QUERY = ComputerQuery

    @staticmethod
    def _create_instance(model, attributes):
        return model(**attributes)

    @staticmethod
    def _insert_instance_to_db(instance):
        with db_context() as session:
            session.add(instance)
            session.commit()
            return instance.id

    def _get_list_instances(self, model, attr_sets):
        return [self._create_instance(model, self._get_attributes(attr_set)) for attr_set in attr_sets]

    def _get_attributes(self, object_info: dict) -> dict:
        model_attributes = {}

        for key, value in object_info.items():
            model = DbTables.get_models().get(key)

            if not value:
                value = None

            elif isinstance(value, (list, tuple)):
                value = self._get_list_instances(model, value)

            elif isinstance(value, dict):
                current_json_layer = object_info[key]
                attributes = self._get_attributes(current_json_layer)
                value = self._create_instance(model, attributes)

            model_attributes[key] = value

        return model_attributes

    @staticmethod
    def _get_valid_data(json_data):
        data = json.loads(json_data)
        valid_data = ComputerValidation(**data)
        if valid_data:
            return data
        raise ValidDataError("Data is not valid")

    def insert_computer_db(self, json_data):
        try:
            valid_data = self._get_valid_data(json_data)
            computer_attributes = self._get_attributes(valid_data)
            computer_instance = self._create_instance(Computer, computer_attributes)
            instance_id = self._insert_instance_to_db(computer_instance)
            return instance_id
        except InsertError:
            raise InsertError("Insert is failed")

