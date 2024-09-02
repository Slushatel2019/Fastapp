import os
from dotenv import load_dotenv


class Credentials:

    def __init__(self, user_name, password, host, port, database) -> None:
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def get(self):
        return {'user_name': self.user_name,
                'password': self.password,
                'host': self.host,
                'port': self.port,
                'database': self.database}


load_dotenv()

cred = Credentials(os.environ.get("USER_NAME"), os.environ.get(
    "PASSWORD"), os.environ.get("HOST"), os.environ.get("PORT"), os.environ.get('DATABASE'))
