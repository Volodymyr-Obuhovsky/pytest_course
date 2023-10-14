# Example of custom validation by pydantic
from typing import List

from pydantic import PastDate, FutureDate
from pydantic.networks import IPv4Network, IPv6Network
from app.src.enums.global_enums import Status
from app.schemas.pydantic.computers.valid_base_model import ValidBaseModel
from app.schemas.pydantic.computers.computer_physical_properties import ComputerPhysicalProperties
from app.schemas.pydantic.computers.computer_owners import ComputerOwners


class DetailedInfo(ValidBaseModel):
    physical: ComputerPhysicalProperties
    owners: List[ComputerOwners]


class ComputerValidation(ValidBaseModel):
    status: Status
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Network
    host_v6: IPv6Network
    detailed_info: DetailedInfo
