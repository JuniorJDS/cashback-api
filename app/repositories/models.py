from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
import sqlalchemy.dialects.postgresql as postgresql
from sqlalchemy.sql import func
from .orm import Base
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    fullName = Column(String(64), index=True)
    email = Column(String(120), unique=True, index=True, nullable=False)
    cpf = Column(String(11), unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    purchase = relationship("Purchase", back_populates="owner")

class Purchase(Base):
    __tablename__ = "purchase"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    cod = Column(String, index=True)
    price = Column(Float, index=True)
    data = Column(DateTime, default=func.now())
    percentCashBack = Column(Integer, index=True)
    valueCashBack = Column(Float, index=True)
    status = Column(String(12), index=True)

    userId = Column(postgresql.UUID(as_uuid=True), ForeignKey("users.id"))
    owner = relationship("User", back_populates="purchase")
