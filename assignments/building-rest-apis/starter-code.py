"""Starter API for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(
    title="School Library API",
    description="An API for managing books in the school library.",
)


books = [
    {
        "id": 1,
        "title": "The Giver",
        "author": "Lois Lowry",
        "available": True,
    },
    {
        "id": 2,
        "title": "A Wrinkle in Time",
        "author": "Madeleine L'Engle",
        "available": False,
    },
]


class BookCreate(BaseModel):
    """Fields required when a client creates a book."""

    title: str
    author: str
    available: bool = True


@app.get("/")
def read_root():
    """Return a welcome message for the API."""

    return {"message": "Welcome to the School Library API"}


@app.get("/books")
def read_books():
    """Return every book in the library."""

    # TODO: Return the books list.
    return books


@app.get("/books/{book_id}")
def read_book(book_id: int):
    """Return one book or a 404 response when it is not found."""

    # TODO: Find the book whose ID matches book_id.
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found",
    )


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    """Add a validated book to the library and return it."""

    # TODO: Choose the next ID and append the new book to books.
    next_id = max(existing_book["id"] for existing_book in books) + 1
    new_book = {"id": next_id, **book.model_dump()}
    books.append(new_book)
    return new_book