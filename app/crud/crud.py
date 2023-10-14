from app.conect_with_db import db_context, inspector
from app.models import User, Computer, DetailedInfo, Physical, Owners


class Crud:
    DB_TABLE = None

    @classmethod
    def get_column_names(cls):
        columns = inspector.get_columns(cls.DB_TABLE.__tablename__)
        return [column["name"] for column in columns if column["name"] != "id"]

    @classmethod
    def get_all_instances(cls):
        with db_context() as session:
            all_instances = session.query(cls.DB_TABLE).all()
            return all_instances

    @classmethod
    def get_instance(cls, instance_id):
        with db_context() as session:
            instance = session.query(cls.DB_TABLE).filter(instance_id == cls.DB_TABLE.id).first()
            return instance

    @classmethod
    def add_instance(cls, new_instance):
        with db_context() as session:
            session.add(new_instance)
            session.commit()
            return new_instance.id

    @classmethod
    def update_instance(cls, instance_id, new_instance_data):
        with db_context() as session:
            instance = session.query(cls.DB_TABLE).filter(cls.DB_TABLE.id == instance_id).first()
            instance_attributes = instance.__dict__
            instance_attributes.update(new_instance_data)
            session.add(instance(**instance_attributes))
            session.commit()

    @classmethod
    def delete_instance(cls, instance_id):
        with db_context() as session:
            instance = session.query(cls.DB_TABLE).filter(cls.DB_TABLE.id == instance_id).first()
            if instance:
                session.delete(instance)
                session.commit()

    @classmethod
    def instances_quantity(cls):
        with db_context() as session:
            quantity = len(session.query(cls.DB_TABLE).all())
            return quantity

    @classmethod
    def delete_all_instances(cls):
        with db_context() as session:
            all_instances = session.query(cls.DB_TABLE).all()
            for instance in all_instances:
                session.delete(instance)
                session.commit()


class UserQuery(Crud):
    DB_TABLE = User


class ComputerQuery(Crud):
    DB_TABLE = Computer


class DetailedInfoQuery(Crud):
    DB_TABLE = DetailedInfo


class PhysicalQuery(Crud):
    DB_TABLE = Physical


class OwnersQuery(Crud):
    DB_TABLE = Owners
