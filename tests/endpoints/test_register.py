import json
from faker import Faker

from app.config.settings import settings

fake = Faker()


def test_register_user(client):
    """
    """
    user = {
        "fullName": fake.name(),
        "cpf": '12233638728',
        "email": fake.email(),
        "password": fake.password()
    }
    response = client.post(f"{settings.API_V1}/auth/register", data=json.dumps(user))
    assert response.status_code == 201


def test_register_user_with_same_cpf(client):
    """
    """
    user = {
        "fullName": fake.name(),
        "cpf": '12233638728',
        "email": fake.email(),
        "password": fake.password()
    }
    response = client.post(f"{settings.API_V1}/auth/register", data=json.dumps(user))
    assert response.status_code == 400