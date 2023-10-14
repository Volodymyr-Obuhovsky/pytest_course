from faker import Faker
from random import shuffle
from app.src.baseclasses.builder_base_class import BuilderBaseClass
from app.src.generators.address_generator import get_fake_address

fake_person = Faker()


class FakeUser(BuilderBaseClass):

    def __init__(self, ):
        super().__init__()
        self.properties = {}

    def _set_user_name(self, name="John"):
        self.properties["user_name"] = fake_person.simple_profile()["username"]
        return self

    def _set_user_password(self, password="123456"):
        if isinstance(password, str):
            password = list(password)
        shuffle(password)
        self.properties["password"] = "".join(password)
        return self

    def _set_user_phone(self, phone="23456"):
        self.properties["phone"] = fake_person.phone_number()
        return self

    def _set_user_address(self, address=None):
        self.properties["address"] = get_fake_address()
        return self

    def _set_work_history(self, work_history=None):
        self.properties["work_history"] = work_history
        return self

    def _set_all_properties(self):
        self._set_user_name()
        self._set_user_password()
        self._set_user_phone()
        self._set_user_address()
        self._set_work_history()

    def create(self):
        self._set_all_properties()
        return self.properties
