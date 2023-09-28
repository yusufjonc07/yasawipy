from pydantic import BaseModel


class NewProduct(BaseModel):
    name: str