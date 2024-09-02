from sqlalchemy import Column, Integer, String

from .database import Base


class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
