"""Controller for Book endpoints."""

from typing import Sequence

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException

from app.controllers import duplicate_error_handler, not_found_error_handler
from app.dtos.book import BookCreateDTO, BookReadDTO, BookUpdateDTO
from app.models import Book
from app.repositories.book import BookRepository, provide_book_repo

ALLOWED_LANGUAGES = {"es", "en", "fr", "de", "it", "pt"}


class BookController(Controller):
    """Controller for book management operations."""

    path = "/books"
    tags = ["books"]
    return_dto = BookReadDTO
    dependencies = {"books_repo": Provide(provide_book_repo)}
    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

    @get("/")
    async def list_books(self, books_repo: BookRepository) -> Sequence[Book]:
        """Get all books."""
        return books_repo.list()

    @get("/{id:int}")
    async def get_book(self, id: int, books_repo: BookRepository) -> Book:
        """Get a book by ID."""
        return books_repo.get(id)

    @post("/", dto=BookCreateDTO)
    async def create_book(self, data: DTOData[Book], books_repo: BookRepository) -> Book:
        """Create a new book."""
        if data.stock <= 0:
            raise HTTPException(status_code=400, detail="Stock must be greater than 0.")
        if data.language not in ALLOWED_LANGUAGES:
            raise HTTPException(status_code=400, detail=f"Language must be one of: {', '.join(ALLOWED_LANGUAGES)}")

        book_instance = data.create_instance()
        return books_repo.add(book_instance)

    @patch("/{id:int}", dto=BookUpdateDTO)
    async def update_book(self, id: int, data: DTOData[Book], books_repo: BookRepository) -> Book:
        """Update a book by ID."""
        raw_obj = data.as_builtins()
        if "stock" in raw_obj and raw_obj["stock"] < 0:
            raise HTTPException(status_code=400, detail="Stock cannot be negative.")
        if "language" in raw_obj and raw_obj["language"] not in ALLOWED_LANGUAGES:
            raise HTTPException(status_code=400, detail=f"Language must be one of: {', '.join(ALLOWED_LANGUAGES)}")

        obj = books_repo.update(Book(id=id, **raw_obj))
        return obj

    @delete("/{id:int}", return_dto=None)
    async def delete_book(self, id: int, books_repo: BookRepository) -> None:
        """Delete a book by ID."""
        books_repo.delete(id)