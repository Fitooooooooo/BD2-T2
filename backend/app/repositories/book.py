"""Repository for Book model."""

from typing import Sequence

from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models import Book, Category, Review


class BookRepository(SQLAlchemySyncRepository[Book]):
    """Book repository."""

    model_type = Book

    async def get_available_books(self) -> Sequence[Book]:
        """Return books with stock > 0."""
        return await self.list(self.model_type.stock > 0)

    async def find_by_category(self, category_id: int) -> Sequence[Book]:
        """Find books by category."""
        statement = select(self.model_type).join(Category, self.model_type.categories).where(Category.id == category_id)
        return await self.list(statement=statement)

    async def get_most_reviewed_books(self, limit: int = 10) -> Sequence[Book]:
        """Return books ordered by the number of reviews."""
        statement = (
            select(self.model_type)
            .join(Review, self.model_type.reviews, isouter=True)
            .group_by(self.model_type.id)
            .order_by(func.count(Review.id).desc())
            .limit(limit)
        )
        return await self.list(statement=statement)

    async def update_stock(self, book_id: int, quantity: int) -> Book:
        """Update the stock of a book."""
        book = await self.get(book_id)
        if book.stock + quantity < 0:
            raise ValueError("Stock cannot be negative.")
        book.stock += quantity
        return await self.update(book)

    async def search_by_author(self, author_name: str) -> Sequence[Book]:
        """Search books by author name (partial, case-insensitive)."""
        return await self.list(self.model_type.author.ilike(f"%{author_name}%"))


async def provide_book_repo(db_session: Session) -> BookRepository:
    """Provide book repository instance with auto-commit."""
    return BookRepository(session=db_session, auto_commit=True)
