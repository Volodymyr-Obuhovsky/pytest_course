# Example of custom validation by pydantic
import re
from pydantic import BaseModel, Field, field_validator


class UserValidation(BaseModel):
    # Default field validate example
    user_name: str = Field(min_length=0)
    email: str = Field()
    phone: str = Field()

    @field_validator("user_name")
    @classmethod
    # Custom field "user_name" validate example
    def user_name_custom_validate(cls, value):
        if not isinstance(value, str):
            raise TypeError("user_name is not string")
        if not value.isalnum():
            raise ValueError("There are specific symbols in user_name")
        return value

    @field_validator("email")
    @classmethod
    # Custom field "email" validate example
    def email_custom_validate(cls, value):
        email_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(email_pattern, value):
            raise ValueError("email not validated")
        return value

    class Config:
        from_attributes = True

    def model_to_dict(self):
        return self.model_dump()
