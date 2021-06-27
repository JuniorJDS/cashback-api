from app.services.security import encrypt, decrypt


def test_encrypt_decrypt_email():
    """ """

    email = 'test@mail.com'

    email_decrypt = decrypt(encrypt(email))

    assert email_decrypt == email


def test_encrypt_decrypt_password():
    """ """

    password = 'sync$@!-_908*JaçÇ'

    password_decrypt = decrypt(encrypt(password))

    assert password_decrypt == password


def test_encrypt_decrypt_cpf():
    """ """

    cpf = '15350946056,'

    cpf_decrypt = decrypt(encrypt(cpf))

    assert cpf_decrypt == cpf
