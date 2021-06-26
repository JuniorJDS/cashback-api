from pydantic import BaseModel


class PurchaseBody(BaseModel):
    cod: str
    price: float
    cpf: str


class PurchaseDb(PurchaseBody):
    status: str