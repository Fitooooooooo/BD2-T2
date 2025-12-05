"""Controller for Review endpoints."""

from typing import Sequence

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException

from app.controllers import duplicate_error_handler, not_found_error_handler
from app.dtos.review import ReviewCreateDTO, ReviewReadDTO, ReviewUpdateDTO
from app.models import Review, User
from app.repositories.review import ReviewRepository, provide_review_repo


class ReviewController(Controller):
    """Controller for review management operations."""

    path = "/reviews"
    tags = ["reviews"]
    return_dto = ReviewReadDTO
    dependencies = {"reviews_repo": Provide(provide_review_repo)}
    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

    @get("/")
    async def list_reviews(self, reviews_repo: ReviewRepository) -> Sequence[Review]:
        """Get all reviews."""
        return reviews_repo.list()

    @get("/{id:int}")
    async def get_review(self, id: int, reviews_repo: ReviewRepository) -> Review:
        """Get a review by ID."""
        return reviews_repo.get(id)

    @post("/", dto=ReviewCreateDTO)
    async def create_review(
        self, data: DTOData[Review], reviews_repo: ReviewRepository, current_user: User
    ) -> Review:
        """Create a new review."""
        if not 1 <= data.rating <= 5:
            raise HTTPException(status_code=400, detail="Rating must be between 1 and 5.")

        review_count = reviews_repo.count(user_id=current_user.id, book_id=data.book_id)
        if review_count >= 3:
            raise HTTPException(
                status_code=400, detail="User cannot create more than 3 reviews for the same book."
            )

        review_data = data.as_builtins()
        review_data["user_id"] = current_user.id
        return reviews_repo.add(Review(**review_data))

    @patch("/{id:int}", dto=ReviewUpdateDTO)
    async def update_review(
        self, id: int, data: DTOData[Review], reviews_repo: ReviewRepository
    ) -> Review:
        """Update a review by ID."""
        raw_obj = data.as_builtins()
        obj = reviews_repo.update(Review(id=id, **raw_obj))
        return obj

    @delete("/{id:int}", return_dto=None)
    async def delete_review(self, id: int, reviews_repo: ReviewRepository) -> None:
        """Delete a review by ID."""
        reviews_repo.delete(id)