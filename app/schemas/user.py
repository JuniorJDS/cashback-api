from pydantic import BaseModel


class UserBody(BaseModel):
    name: str
    cpf: str
    email: str
    password: str