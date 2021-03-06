import aiohttp

from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from starlette import status
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN

from app.schemas.purchase import PurchaseBody, PurchaseCreate, PurchaseUpdate
from app.repositories import models
from app.routes.deps import get_current_user, get_db
from app.entity.cashback import cash
from app.repositories.purchaseRepository import purchaseDb
from app.services.httpClient import httpClient
#from loguru import logger


router = APIRouter()


responses = {
    400: {},
    404: {},
    500: {}
}


async def _validation(db, id, user):
    """ Validações para usuario e compra """
    obj = purchaseDb.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Compra não encontrada.")
    
    if user.id != obj.userId:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Acesso Negado.")

    if obj.status != 'Em validação':
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="A compra não está mais Em Validação.")
    
    return obj


@router.post('', summary='Cadastrar Compra', status_code=HTTP_201_CREATED, responses={**responses})
async def register_purchase(
    purchase: PurchaseBody,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
    ):
    """
    Endpoint responsável por retornar os usuários cadastrados no
    banco de dados.
    """
    if user.cpf == '15350946056':
        status='Aprovado'
    else:
        status = 'Em validação'
    
    value, percent = cash.compute_cashback(purchase.price)

    _purchase = {
        "userId": user.id,
        **purchase.dict(),
        "percentCashBack": percent,
        "valueCashBack": value,
        "status": status
        }

    obj = purchaseDb.create(db, purchase=PurchaseCreate(**_purchase))
    return obj


@router.get('', summary='Listar Compras Cadastradas', responses={**responses})
async def list_purchases(
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
    ):
    """
    Endpoint responsável por retornar os usuários cadastrados no
    banco de dados.
    """

    obj = purchaseDb.list_by_user(db, userId=user.id)
    return obj


@router.put('/{id}', summary='Editar compra "Em Validação"', responses={**responses})
async def update_purchase_by_id(
    id: str,
    purchase: PurchaseUpdate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
    ):
    """
    Endpoint responsável por editar compra em validação.
    """
    """
    obj = purchaseDb.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Compra não encontrada.")
    
    if user.id != obj.userId:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Acesso Negado.")

    """
    _ = await _validation(db, id, user)

    value, percent = cash.compute_cashback(purchase.price)

    _purchase = {
            key: value for key, value in purchase if value
        }

    purchase_update = {
        **_purchase,
        "percentCashBack": percent,
        "valueCashBack": value
        }

    obj_updated = purchaseDb.update(db, id, purchase_update)
    return obj_updated


@router.delete('/{id}', summary='Deletar compra "Em Validação"', responses={**responses})
async def delete_purchase_by_id(
    id: str,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
    ):
    """
    Endpoint responsável por deletar compra em validação.
    """
    """
    obj = purchaseDb.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Compra não encontrada.")
    
    if user.id != obj.userId:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Acesso Negado.")
    """
    obj = await _validation(db, id, user)
    purchaseDb.delete(db, obj)
    return {"message": "compra Removida"}


@router.get('/acumCashback', summary='Cashback Acumulado', responses={**responses})
async def list_acum_cashback(
    user: models.User = Depends(get_current_user),
    client: aiohttp.ClientSession = Depends(httpClient)
):
    """
    Endpoint responsável por retornar o cashback acumulado do usuário.
    """
    request = await client.get(f'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={user.cpf}')
    r = await request.json()

    status = r.get('statusCode') 
    if  status != 200:
        raise HTTPException(status_code=status, detail=r.get('body'))

    result = {
        "fullName": user.fullName,
        "email": user.email,
        "cpf": user.cpf,
        "acumCashback": r.get('body')['credit']
    }
    return result
