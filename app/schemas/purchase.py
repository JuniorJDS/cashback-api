from typing import Optional
from pydantic import BaseModel
from datetime import date
from uuid import UUID


class PurchaseBody(BaseModel):
    cod: str
    price: float
    data: date


class PurchaseCreate(PurchaseBody):
    percentCashBack: int
    valueCashBack: float
    userId: UUID
    status: str


class PurchaseUpdate(BaseModel):
    cod: Optional[str] = None
    price: Optional[float] = None
    data: Optional[date] = None
