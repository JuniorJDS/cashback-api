from typing import Generator
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from app.config.settings import settings
from app.repositories.orm import SessionLocal


oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1}/auth/login"
)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()