import pytest
import json
from typing import Generator

from starlette.testclient import TestClient
from faker import Faker

from app.main import app
from app.repositories.userRepository import userDb
from app.repositories.purchaseRepository import purchaseDb
from app.repositories.purchaseRepository import PurchaseCreate
from app.schemas.user import UserCreate
from app.repositories.orm import SessionLocal
from app.config.settings import settings

fake = Faker()

@pytest.fixture(scope='module')
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope='session')
def user(db):
    user = {
        "fullName": fake.name(),
        "cpf": "11111111117",
        "email": fake.email(),
        "password": fake.password()

    }
    
    result = userDb.create(db, UserCreate(**user))

    yield result, user
    userDb.delete(db, result)


@pytest.fixture(scope='session')
def purchase(db, user):

    user, _ = user

    purchase = {
        "cod": "ABC123",
        "price": 2000.0,
        "data": "2020-01-01",
        "percentCashBack": 20,
        "valueCashBack": 2.0,
        "userId": user.id,
        "status": "Em validação"
    }

    obj = purchaseDb.create(db, purchase=PurchaseCreate(**purchase))

    yield obj
    purchaseDb.delete(db, obj)


@pytest.fixture(scope='module')
def token(client, user):

    user, _user = user

    login = {
        "username": user.email,
        "password": _user['password']
    }
    
    r = client.post(f"{settings.API_V1}/auth/login", data=login)
    response = r.json()

    auth_token = response["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    return headers
