from app.repositories.userRepository import userDb
from app.schemas.user import UserCreate


def test_get_by_email(db, user, purchase):

    user, _ = user
    result = userDb.get_by_email(db, user.email)

    assert result.fullName == user.fullName
    assert result.email == user.email
    assert result.cpf == user.cpf


def test_get_by_id(db, user):

    user, _ = user
    result = userDb.get_by_id(db, user.id)

    assert result.fullName == user.fullName
    assert result.email == user.email
    assert result.cpf == user.cpf


def test_authenticate_true(db, user):

    user, user_bf_db = user
    result = userDb.authenticate(db, user.email, user_bf_db['password'])

    assert result.fullName == user.fullName
    assert result.email == user.email
    assert result.cpf == user.cpf


def test_authenticate_false(db, user):

    user, _ = user
    result = userDb.authenticate(db, user.email, 'sem_senha')

    assert result is None
