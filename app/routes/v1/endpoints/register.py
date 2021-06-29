from datetime import timedelta

from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from app.schemas.user import UserCreate, UserLogin
from app.routes.deps import get_db
from app.repositories.sqlAlchemyRepository import userDb
from app.services.security import create_access_token
from app.config.settings import settings
from fastapi.security import OAuth2PasswordRequestForm
#from loguru import logger


router = APIRouter()


responses = {
    400: {},
    404: {},
    500: {}
}


@router.post('/register', summary='register', status_code=HTTP_201_CREATED, responses={**responses})
async def create_user(userInfo: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint responsável por cadastrar um novo revendedor(a)

    Parâmetros:
    - **fullName**: nome do revendedor(a).
    - **cpf**: cpf válido do revendedor(a).
    - **email**: email do revendedor(a).
    - **password**: senha de acesso.
    """
    try:
    
        object = userDb.create(db, userInfo)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Não foi possível inserir.")

    return object


@router.post('/login', summary='login', responses={**responses})
async def register_user(
    #user: UserLogin, 
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
    ):
    """
    Endpoint responsável por logar um revendedor e validar suas credenciais.

    Parâmetros:
    - **email**: email do revendedor(a).
    - **password**: senha de acesso.
    """
    user = userDb.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Email ou Password incorreto.")


    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            user.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
