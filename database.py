from sqlalchemy import create_engine, URL
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.sql import func
from functools import cached_property
from .credentials import cred
from . import schemas
from .models.book import Book
from .logs.logger import logger


class Database:

    @cached_property
    def url_object(self):
        self.cred = cred.get()

        url_object = URL.create(
            "postgresql",
            username=self.cred['user_name'],
            password=self.cred['password'],
            host=self.cred['host'],
            database=self.cred['database'],
        )
        return url_object

    @cached_property
    def engine(self):
        return create_engine(self.url_object)

    @cached_property
    def session(self):
        Session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine)
        return Session()

    def get_books(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(Book).offset(skip).limit(limit).all()

    def get_random_book(self, db: Session):
        return db.query(Book).order_by(func.random()).first()

    def get_book_by_id(self, db: Session, book_id: int):
        return db.query(Book).filter(Book.id == book_id).first()

    def create_book(self, db: Session, book: schemas.CreateBook):
        is_exist_name = db.query(Book).filter(
            Book.name == book.name).first().name
        if is_exist_name:
            return False
        db_book = Book(name=book.name)
        db.add(db_book)
        db.commit()
        logger.info("book %s is added", book.name)
        db.refresh(db_book)
        return db_book
