from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .credentials import cred


cred = cred.get()

SQLALCHEMY_DATABASE_URL = f"postgresql://{cred['user_name']}:{cred['password']}@{cred['host']}:{cred['port']}/{cred['database']}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
