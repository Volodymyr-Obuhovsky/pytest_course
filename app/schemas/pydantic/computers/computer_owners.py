# Example of custom validation by pydantic

from pydantic import PaymentCardNumber, EmailStr
from app.schemas.pydantic.computers.valid_base_model import ValidBaseModel


class ComputerOwners(ValidBaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr
