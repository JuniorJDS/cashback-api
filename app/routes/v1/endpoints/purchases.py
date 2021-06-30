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
#from loguru import logger


router = APIRouter()


responses = {
    400: {},
    404: {},
    500: {}
}


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
    obj = purchaseDb.list_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Compra não encontrada.")
    
    if user.id != obj.userId:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Acesso Negado.")

    _purchase = {
            key: value for key, value in purchase if value
        }
    print(_purchase.values())
    obj_updated = None#_purchase.value()#purchaseDb.update(db, id, PurchaseUpdate(**_purchase.values))
    
    
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
    obj = purchaseDb.list_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Compra não encontrada.")
    
    if user.id != obj.userId:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Acesso Negado.")
    
    purchaseDb.delete(db, obj)
    
    return {"message": "compra Removida"}


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
