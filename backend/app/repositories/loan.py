"""Repository for Loan model."""

from datetime import date
from decimal import Decimal
from typing import Sequence

from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Loan, LoanStatus
from app.repositories.book import BookRepository


class LoanRepository(SQLAlchemySyncRepository[Loan]):
    """Loan repository."""

    model_type = Loan

    async def get_active_loans(self) -> Sequence[Loan]:
        """Return active loans."""
        return await self.list(self.model_type.status == LoanStatus.ACTIVE)

    async def get_overdue_loans(self) -> Sequence[Loan]:
        """Return overdue loans and update their status."""
        statement = select(self.model_type).where(
            self.model_type.due_date < date.today(),
            self.model_type.status == LoanStatus.ACTIVE,
        )
        overdue_loans = await self.list(statement=statement)
        for loan in overdue_loans:
            loan.status = LoanStatus.OVERDUE
            await self.update(loan)
        return overdue_loans

    async def calculate_fine(self, loan: Loan) -> Decimal:
        """Calculate fine for an overdue loan."""
        if loan.due_date >= date.today():
            return Decimal(0)

        days_overdue = (date.today() - loan.due_date).days
        fine = Decimal(days_overdue * 500)
        return min(fine, Decimal(50000))

    async def return_book(self, loan_id: int, book_repo: BookRepository) -> Loan:
        """Process a book return."""
        loan = await self.get(loan_id, auto_expunge=True)
        if loan.status == LoanStatus.RETURNED:
            raise ValueError("Book has already been returned.")

        loan.status = LoanStatus.RETURNED
        loan.return_dt = date.today()

        if loan.due_date < loan.return_dt:
            loan.fine_amount = await self.calculate_fine(loan)

        await book_repo.update_stock(loan.book_id, 1)
        return await self.update(loan)

    async def get_user_loan_history(self, user_id: int) -> Sequence[Loan]:
        """Get the complete loan history for a user, ordered by date."""
        return await self.list(self.model_type.user_id == user_id, order_by=self.model_type.loan_dt.desc())


async def provide_loan_repo(db_session: Session) -> LoanRepository:
    """Provide loan repository instance with auto-commit."""
    return LoanRepository(session=db_session, auto_commit=True)
