import os
from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    """ Configurações globais """

    API_V1: str = "/api/v1"
    SECRET_KEY: str = 'PrHWIkt3sLDY6l7xA0A7WaaNeKoLVUKDlYAyGAgLIng='


settings = Settings()