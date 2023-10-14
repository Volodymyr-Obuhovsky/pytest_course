class BaseService:
    DB_TABLE = None
    DB_TABLE_QUERY = None

    @classmethod
    def read_column_names(cls):
        return cls.DB_TABLE_QUERY.get_column_names()

    @classmethod
    def read_all_instances(cls):
        all_instances = cls.DB_TABLE_QUERY.get_all_instances()
        return all_instances

    @classmethod
    def read_instance(cls, instance_id):
        instance_id = cls.DB_TABLE_QUERY.get_instance(instance_id)
        return instance_id

    @classmethod
    def create_instance(cls, valid_instance):
        new_data = valid_instance.model_to_dict()
        new_instance = cls.DB_TABLE(**new_data)
        instance = cls.DB_TABLE_QUERY.add_instance(new_instance)
        return instance

    @classmethod
    def update_instance_data(cls, instance_id: int, new_valid_instance_data):
        new_instance_data = new_valid_instance_data.model_to_dict()
        cls.DB_TABLE_QUERY.update_instance(instance_id, new_instance_data)

    @classmethod
    def del_all_instances(cls):
        cls.DB_TABLE_QUERY.delete_all_instances()

    @classmethod
    def del_instance(cls, user_id):
        cls.DB_TABLE_QUERY.delete_instance(user_id)

    @classmethod
    def get_instances_quantity(cls):
        quantity = cls.DB_TABLE_QUERY.instances_quantity()
        return quantity
