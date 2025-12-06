"""Controller for Loan endpoints."""

from datetime import date, timedelta
from typing import Sequence, Any

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.enums import RequestEncodingType
from litestar.exceptions import HTTPException

from app.controllers import duplicate_error_handler, not_found_error_handler
from app.dtos.loan import LoanCreateDTO, LoanReadDTO, LoanUpdateDTO
from app.models import Loan
from app.repositories.loan import LoanRepository, provide_loan_repo

from app.repositories.book import BookRepository, provide_book_repo

class LoanController(Controller):
    """Controller for loan management operations."""

    path = "/loans"
    tags = ["loans"]
    return_dto = LoanReadDTO
    dependencies = {"loans_repo": Provide(provide_loan_repo), "books_repo": Provide(provide_book_repo)}
    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

    @get("/")
    async def list_loans(self, loans_repo: LoanRepository) -> Sequence[Loan]:
        """Get all loans."""
        return loans_repo.list()

    @get("/{id:int}")
    async def get_loan(self, id: int, loans_repo: LoanRepository) -> Loan:
        """Get a loan by ID."""
        return loans_repo.get(id)

    @post("/", dto=LoanCreateDTO)
    async def create_loan(
        self,
        data: DTOData[Loan],
        loans_repo: LoanRepository,
    ) -> Loan:
        """Create a new loan."""
        loan_data = data.as_builtins()
        loan_data["due_date"] = date.today() + timedelta(days=14)

        new_loan = Loan(**loan_data)

    @patch("/{id:int}", dto=LoanUpdateDTO)
    async def update_loan(
        self,
        id: int,
        data: DTOData[Loan],
        loans_repo: LoanRepository,
    ) -> Loan:
        """Update a loan by ID."""
        raw_obj = data.as_builtins()
        obj = loans_repo.update(Loan(id=id, **raw_obj))

        return obj

    @get("/active")
    async def get_active_loans(self, loans_repo: LoanRepository) -> Sequence[Loan]:
        """Get all active loans."""
        return await loans_repo.get_active_loans()

    @get("/overdue")
    async def get_overdue_loans(self, loans_repo: LoanRepository) -> Sequence[Loan]:
        """Get all overdue loans."""
        return await loans_repo.get_overdue_loans()
    
    @post("/{loan_id:int}/return")
    async def return_book(self, loan_id: int, loans_repo: LoanRepository, books_repo: BookRepository) -> Loan:
        """Return a loaned book."""
        try:
            returned_loan = await loans_repo.return_book(loan_id, books_repo)
            return returned_loan
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    @get("/{loan_id:int}/calculate-fine")
    async def calculate_fine(self, loan_id: int, loans_repo: LoanRepository) -> dict[str, Any]:
         """Calculate the fine for a loan."""
         loan = await loans_repo.get(loan_id)
         fine = await loans_repo.calculate_fine(loan)
         return {"fine_amount": fine}

    @get("/user/{user_id:int}")
    async def get_user_loan_history(self, user_id: int, loans_repo: LoanRepository) -> Sequence[Loan]:
        """Get loan history for a specific user."""
        return await loans_repo.get_user_loan_history(user_id)



    





    @delete("/{id:int}", return_dto=None, )
    async def delete_loan(self, id: int, loans_repo: LoanRepository) -> None:
        """Delete a loan by ID."""
        loans_repo.delete(id)
