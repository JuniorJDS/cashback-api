import json

from fastapi.param_functions import Header
from app.config.settings import settings


def test_list_purchase(client, token):
    
    
    response = client.get(f"{settings.API_V1}/purchases", headers=token)#json.dumps(user))
    
    assert response.status_code == 200