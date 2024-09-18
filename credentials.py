import os
from dotenv import load_dotenv
from dataclasses import dataclass
from .logs.logger import logger


@dataclass
class Credentials:
    user_name: str
    password: str
    host: int
    port: int
    database: str

    def get(self):
        return {'user_name': self.user_name,
                'password': self.password,
                'host': self.host,
                'port': self.port,
                'database': self.database}


load_dotenv()

cred = Credentials(os.environ.get("USER_NAME"),
                   os.environ.get("PASSWORD"),
                   os.environ.get("HOST"),
                   os.environ.get("PORT"),
                   os.environ.get('DATABASE'))
logger.info('credentials successfully loaded')
