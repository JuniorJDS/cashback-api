from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
#from loguru import logger




router = APIRouter()


responses = {
    400: {},
    404: {},
    500: {}
}


@router.get('', summary='Hello', responses={**responses})
async def hello():
    """
    Endpoint responsável por retornar os usuários cadastrados no
    banco de dados.
    """
    return "ola"
