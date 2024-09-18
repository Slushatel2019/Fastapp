from .logs.logger import logger
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .models import book
from . import schemas
from .database import Database


Database = Database()
book.Base.metadata.create_all(bind=Database.engine)

app = FastAPI()


# Dependency
def get_db():
    db = Database.session
    try:
        yield db
    finally:
        db.close()


@app.get("/books/", response_model=list[schemas.Book])
def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = Database.get_books(db, skip=skip, limit=limit)
    if books is None:
        logger.warning("No books at all in get_books")
        raise HTTPException(status_code=404, detail="Book not found")
    return books


@app.get("/book/", response_model=schemas.Book)
def get_random_book(db: Session = Depends(get_db)):
    book = Database.get_random_book(db)
    if book is None:
        logger.warning("No random book")
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.get("/book/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = Database.get_book_by_id(db, book_id=book_id)
    if book is None:
        logger.warning("Book not found with id %s", book_id)
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/book/", response_model=schemas.CreateBook)
def create_book(book: schemas.CreateBook, db: Session = Depends(get_db)):
    book_created = Database.create_book(db=db, book=book)
    if book_created:
        return book_created
    else:
        logger.warning("book with name %s has already existed", book.name)
        raise HTTPException(
            status_code=422, detail=f"Book with name {book.name} has already existed")
