from cryptography.fernet import Fernet
from app.config.settings import settings

def encrypt(data):
    cipher_suite = Fernet(settings.SECRET_KEY)
    cipher = cipher_suite.encrypt(str.encode(data))
    return cipher

def decrypt(cipher):
    cipher_suite = Fernet(settings.SECRET_KEY)
    data = cipher_suite.decrypt(cipher)#str.encode(cipher))
    return str(data, 'utf-8')