from cryptography.fernet import Fernet
from app.config.settings import settings

from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def encrypt(data):
    cipher_suite = Fernet(settings.SECRET_KEY)
    cipher = cipher_suite.encrypt(str.encode(data))
    return cipher

def decrypt(cipher):
    cipher_suite = Fernet(settings.SECRET_KEY)
    data = cipher_suite.decrypt(cipher)#str.encode(cipher))
    return str(data, 'utf-8')

