# Example of custom validation by pydantic

from pydantic import UUID4
from pydantic.networks import HttpUrl
from pydantic.color import Color
from app.schemas.pydantic.computers.valid_base_model import ValidBaseModel


class ComputerPhysicalProperties(ValidBaseModel):
    color: Color
    photo: HttpUrl
    uuid: UUID4
