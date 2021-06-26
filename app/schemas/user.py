from pydantic import BaseModel


class UserLogin(BaseModel):

    email: str
    password: str

class UserRegister(UserLogin):

    fullName: str
    cpf: str