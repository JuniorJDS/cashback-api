from typing import Generator
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_403_FORBIDDEN
from sqlalchemy.orm import Session
from jose import jwt
from pydantic import ValidationError
from app.config.settings import settings
from app.repositories.orm import SessionLocal
from app.repositories import models
from app.services import security
from app.repositories.userRepository import userDb
from app.schemas.token import TokenPayload


oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1}/auth/login"
)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db), 
    token: str = Depends(oauth2)
) -> models.User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )

        token_data = TokenPayload(**payload)

    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = userDb.get_by_id(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

