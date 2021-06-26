import json
from app.config.settings import settings


def test_register_user(client):
    """
    """
    user = {
        "name": "name-teste",
        "cpf": "12312312312",
        "email": "teste@mail.com",
        "password": "123123123123"
    }
    response = client.post(f"{settings.API_V1}/register", data=json.dumps(user))
    assert response.status_code == 201