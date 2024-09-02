from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CreateBook(BaseModel):
    name: str
