from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from starlette import status
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from app.schemas.purchase import PurchaseBody, PurchaseDb
from app.repositories import models
from app.routes.deps import get_current_user
#from loguru import logger


router = APIRouter()


responses = {
    400: {},
    404: {},
    500: {}
}


@router.post('', summary='Cadastrar Compra', responses={**responses})
async def register_purchase(
    purchase: PurchaseBody,
    user: models.User = Depends(get_current_user)
    ):
    """
    Endpoint responsável por retornar os usuários cadastrados no
    banco de dados.
    """

    if purchase.cpf == '15350946056':
        status='Aprovado'
    
    # chamar services e guardar as informações no Banco
    return "Compra Cadastrada"


@router.get('', summary='Listar Compras Cadastradas', responses={**responses})
async def list_purchases(
    user: models.User = Depends(get_current_user)
    ):
    """
    Endpoint responsável por retornar os usuários cadastrados no
    banco de dados.
    """
    # pega usuario pela autenticação e consulta todas suas compras
    # fake_userId = 'abcd123asder'

    # lista todas as compras
    
    # chamar services e guardar as informações no Banco
    return user


@router.put('/{id}', summary='Editar compra "Em Validação"', responses={**responses})
async def update_purchase_by_id(
    id: str,
    user: models.User = Depends(get_current_user)
    ):
    """
    Endpoint responsável por editar compra em validação.
    """
    # pega usuario pela autenticação e consulta a compra pelo id.
    # fake_userId = 'abcd123asder'

    # se a compra existe
    # chama services para editar a compra
    
    return []


@router.delete('/{id}', summary='Deletar compra "Em Validação"', responses={**responses})
async def delete_purchase_by_id(
    id: str,
    user: models.User = Depends(get_current_user)
    ):
    """
    Endpoint responsável por deletar compra em validação.
    """
    # pega usuario pela autenticação e consulta a compra pelo id.
    # fake_userId = 'abcd123asder'

    # se a compra existe
    # chama services para remover compra
    
    return "compra Removida"


@router.get('/acumCashback', summary='Cashback Acumulado', responses={**responses})
async def list_acum_cashback(
    user: models.User = Depends(get_current_user)
):
    """
    Endpoint responsável por retornar o cashback acumulado do usuário.
    """
    # pega o userId pela autenticação e busca o cpf
    # fake_userId = 'abcd123asder'

    # com o cpf consulta outra API
    
    # retorna o cashback acumulado
    return []
