import json
from app.config.settings import settings


def test_hello(client):
    """
    """

    response = client.get(f"{settings.API_V1}/purchases")
    assert response.status_code == 200