from app.config.settings import settings


def test_register_user_with_same_cpf(client, user):

    _, user = user
    
    
    response = client.post(f"{settings.API_V1}/auth/register", data=user)#json.dumps(user))
    assert response.status_code == 400
