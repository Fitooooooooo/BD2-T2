"""Script to seed the database with initial data."""

from datetime import date, timedelta

from decimal import Decimal
from app.db import sqlalchemy_config
from app.models import Book, Category, Loan, LoanStatus, Review, User
from app.repositories.user import password_hasher


def seed_data() -> None:
    """Populate the database with initial data."""
    print("Starting to seed data...")

    with sqlalchemy_config.get_session() as session:
        # 1. Create Categories
        categories_data = [
            {"name": "Ficción", "description": "Obras literarias de imaginación."},
            {"name": "No Ficción", "description": "Obras basadas en hechos y realidad."},
            {"name": "Ciencia", "description": "Libros sobre temas científicos y tecnológicos."},
            {"name": "Historia", "description": "Libros que exploran eventos pasados."},
            {"name": "Fantasía", "description": "Género con elementos mágicos y sobrenaturales."},
        ]
        categories = [Category(**data) for data in categories_data]
        session.add_all(categories)
        session.flush()
        print(f"Created {len(categories)} categories.")

        # 2. Create Users
        users_data = [
            {
                "username": "johndoe", "fullname": "John Doe", "password": "password123",
                "email": "john.doe@example.com", "phone": "123456789", "address": "123 Main St",
            },
            {
                "username": "janedoe", "fullname": "Jane Doe", "password": "password456",
                "email": "jane.doe@example.com", "phone": "987654321", "address": "456 Oak Ave",
            },
            {
                "username": "peterjones", "fullname": "Peter Jones", "password": "password789",
                "email": "peter.jones@example.com", "phone": "555111222", "address": "789 Pine Ln",
            },
            {
                "username": "marysmith", "fullname": "Mary Smith", "password": "password101",
                "email": "mary.smith@example.com", "phone": "555333444", "address": "101 Maple Rd",
            },
            {
                "username": "admin", "fullname": "Admin User", "password": "adminpassword",
                "email": "admin@example.com", "phone": "555555555", "address": "1 Admin Ct",
            },
        ]
        users = []
        for user_data in users_data:
            user_data["password"] = password_hasher.hash(user_data["password"])
            users.append(User(**user_data))
        session.add_all(users)
        session.flush()
        print(f"Created {len(users)} users.")

        # 3. Create Books
        books_data = []
        for i, num in enumerate(range(1120, 1166, 5)):
            books_data.append({
                "title": f"Libro de Prueba {i + 1}", "author": f"Autor {i + 1}",
                "isbn": f"ISBN-BD2-2025-{num}", "pages": 100 + i * 20, "published_year": 2000 + i,
                "stock": (i % 5) + 1, "language": "es", "publisher": f"Editorial {i + 1}",
                "categories": [categories[i % len(categories)]],
            })
        books = [Book(**data) for data in books_data]
        session.add_all(books)
        session.flush()
        print(f"Created {len(books)} books.")

        # 4. Create Loans
        today = date.today()
        loans_data = [
            # Active loan
            {"user_id": users[0].id, "book_id": books[0].id, "loan_dt": today - timedelta(days=5), "due_date": today + timedelta(days=9), "status": LoanStatus.ACTIVE},
            # Returned loan
            {"user_id": users[1].id, "book_id": books[1].id, "loan_dt": today - timedelta(days=20), "return_dt": today - timedelta(days=10), "due_date": today - timedelta(days=6), "status": LoanStatus.RETURNED},
            # Overdue loan
            {"user_id": users[2].id, "book_id": books[2].id, "loan_dt": today - timedelta(days=30), "due_date": today - timedelta(days=16), "status": LoanStatus.OVERDUE},
            # Another active loan
            {"user_id": users[0].id, "book_id": books[3].id, "loan_dt": today - timedelta(days=2), "due_date": today + timedelta(days=12), "status": LoanStatus.ACTIVE},
            # Returned with fine
            {"user_id": users[3].id, "book_id": books[4].id, "loan_dt": today - timedelta(days=40), "return_dt": today - timedelta(days=5), "due_date": today - timedelta(days=26), "status": LoanStatus.RETURNED, "fine_amount": Decimal("10500.00")},
            # Active, due soon
            {"user_id": users[4].id, "book_id": books[5].id, "loan_dt": today - timedelta(days=13), "due_date": today + timedelta(days=1), "status": LoanStatus.ACTIVE},
            # Returned on time
            {"user_id": users[1].id, "book_id": books[6].id, "loan_dt": today - timedelta(days=15), "return_dt": today - timedelta(days=1), "due_date": today - timedelta(days=1), "status": LoanStatus.RETURNED},
            # Active loan for another user
            {"user_id": users[2].id, "book_id": books[7].id, "loan_dt": today - timedelta(days=1), "due_date": today + timedelta(days=13), "status": LoanStatus.ACTIVE},
        ]
        loans = [Loan(**data) for data in loans_data]
        session.add_all(loans)
        session.flush()
        print(f"Created {len(loans)} loans.")

        # 5. Create Reviews
        reviews_data = [
            {"user_id": users[0].id, "book_id": books[1].id, "rating": 5, "comment": "¡Excelente libro!"},
            {"user_id": users[1].id, "book_id": books[0].id, "rating": 4, "comment": "Muy bueno, lo recomiendo."},
            {"user_id": users[2].id, "book_id": books[2].id, "rating": 3, "comment": "Interesante, pero un poco lento."},
            {"user_id": users[3].id, "book_id": books[3].id, "rating": 5, "comment": "Una obra maestra."},
            {"user_id": users[4].id, "book_id": books[4].id, "rating": 2, "comment": "No me gustó mucho."},
            {"user_id": users[0].id, "book_id": books[2].id, "rating": 4, "comment": "Mejor de lo que esperaba."},
            {"user_id": users[1].id, "book_id": books[3].id, "rating": 5, "comment": "Lo volvería a leer."},
            {"user_id": users[2].id, "book_id": books[4].id, "rating": 4, "comment": "Sólido."},
            {"user_id": users[3].id, "book_id": books[5].id, "rating": 1, "comment": "No es para mí."},
            {"user_id": users[4].id, "book_id": books[6].id, "rating": 5, "comment": "Imprescindible."},
            {"user_id": users[0].id, "book_id": books[7].id, "rating": 4, "comment": "Buen ritmo."},
            {"user_id": users[1].id, "book_id": books[8].id, "rating": 3, "comment": "Regular."},
            {"user_id": users[2].id, "book_id": books[9].id, "rating": 5, "comment": "Fantástico."},
            {"user_id": users[3].id, "book_id": books[0].id, "rating": 4, "comment": "Me enganchó desde el principio."},
            {"user_id": users[4].id, "book_id": books[1].id, "rating": 5, "comment": "De mis favoritos."},
        ]
        reviews = [Review(**data) for data in reviews_data]
        session.add_all(reviews)
        session.flush()
        print(f"Created {len(reviews)} reviews.")

        session.commit()
        print("Data seeding complete.")


if __name__ == "__main__":
    seed_data()
