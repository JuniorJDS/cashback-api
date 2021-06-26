from fastapi import APIRouter
from app.routes.v1.endpoints import purchases, register


endpoint_router = APIRouter()


endpoint_router.include_router(purchases.router, prefix='/purchases', tags=['Compras'])
endpoint_router.include_router(register.router, prefix='/auth', tags=['Authentication'])