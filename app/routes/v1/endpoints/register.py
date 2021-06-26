from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from app.schemas.user import UserBody
from app.services.cryptography import encrypt, decrypt
#from loguru import logger




router = APIRouter()


responses = {
    400: {},
    404: {},
    500: {}
}


@router.post('', summary='register', status_code=HTTP_201_CREATED, responses={**responses})
async def get_register(user: UserBody):
    """
    Endpoint responsável por cadastrar um novo revendedor(a)

    Parâmetros:
    - **name**: nome do revendedor(a).
    - **cpf**: cpf válido do revendedor(a).
    - **email**: email do revendedor(a).
    - **password**: senha de acesso.
    """
    # encripitar cpf, email e password
    # salvar as informações no banco de dados
    print(user.name)
    print(encrypt(user.name))
    return user
