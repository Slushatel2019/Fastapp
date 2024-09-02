from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from . import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Books).offset(skip).limit(limit).all()


def get_random_book(db: Session):
    return db.query(models.Books).order_by(func.random()).first()


def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Books).filter(models.Books.id == book_id).first()


def create_book(db: Session, book: schemas.CreateBook):
    db_book = models.Books(name=book.name)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
