from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from app.schemas.user import UserRegister, UserLogin
#from loguru import logger


router = APIRouter()


responses = {
    400: {},
    404: {},
    500: {}
}


@router.post('/register', summary='register', status_code=HTTP_201_CREATED, responses={**responses})
async def create_user(user: UserRegister):
    """
    Endpoint responsável por cadastrar um novo revendedor(a)

    Parâmetros:
    - **name**: nome do revendedor(a).
    - **cpf**: cpf válido do revendedor(a).
    - **email**: email do revendedor(a).
    - **password**: senha de acesso.
    """
    # recebe os parametros e envia para o Services

    # Se ok, 'Usuário Cadastrado!!!'

    # verificar se já existe o usuário por cpf (chave primária).

    return {'Usuário Cadastrado com Sucesso!'}


@router.post('/login', summary='login', responses={**responses})
async def register_user(user: UserLogin):
    """
    Endpoint responsável por logar um revendedor e validar suas credenciais.

    Parâmetros:
    - **email**: email do revendedor(a).
    - **password**: senha de acesso.
    """
    # recebe os parametros e consulta o banco de dados
    # se não existe - retorna um 404
    # se encontrar - retorna um 200 e token de acesso

    object = {
        'token': 'asdasakjjdksaldkdjskaldkjdkskal'
    }
    return object
