import os
from dotenv import load_dotenv

from dataclasses import dataclass

load_dotenv('./.env')


@dataclass
class Config:
    pass


class DbConnection(Config):
    DB_ENGINE: str = os.getenv('DB_ENGINE')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: int = os.getenv('DB_PORT')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASS: str = os.getenv('DB_PASS')
    DB_NAME: str = os.getenv('DB_NAME')

    @classmethod
    def get_connection_url(cls):
        return f"{cls.DB_ENGINE}://{cls.DB_USER}:{cls.DB_PASS}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
    