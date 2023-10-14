from enum import Enum


class ListValues(Enum):

    @classmethod
    def values_to_list(cls):
        return list(map(lambda attribute: attribute.value, cls))
