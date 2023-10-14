from app.models import User
from app.crud.crud import UserQuery
from app.services.base_service import BaseService


class UserService(BaseService):
    DB_TABLE = User
    DB_TABLE_QUERY = UserQuery

