from enum import Enum

from app.src.enums.list_enums import ListValues


class GlobalErrorMessages(Enum):
    WRONG_USER_QUANTITY = "Wrong number of user's quantity"
    WRONG_DELETE_USER = "There mustn't be users"
    WRONG_ADDED_USER = "Added user is not corresponding to user's data"


class Status(ListValues):
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"



