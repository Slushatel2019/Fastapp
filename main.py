from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@app.get("/book/", response_model=schemas.Book)
def read_random_book(db: Session = Depends(get_db)):
    book = crud.get_random_book(db)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.get("/book/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/book/", response_model=schemas.CreateBook)
def create_book(
    book: schemas.CreateBook, db: Session = Depends(get_db)
):
    return crud.create_book(db=db, book=book)
