from pydantic import BaseModel


class ValidBaseModel(BaseModel):
    class Config:
        from_attributes = True

    def model_to_dict(self):
        return self.model_dump()