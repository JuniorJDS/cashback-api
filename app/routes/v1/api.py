from fastapi import APIRouter
from app.routes.v1.endpoints import purchases


endpoint_router = APIRouter()


endpoint_router.include_router(purchases.router, prefix='/purchases', tags=['Compras'])