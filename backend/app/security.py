"""OAuth2 authentication and security configuration."""

from advanced_alchemy.exceptions import NotFoundError
from litestar.connection import ASGIConnection
from litestar.security.jwt import OAuth2PasswordBearerAuth, Token

from app.config import settings
from app.models import User
from app.repositories.user import UserRepository


async def retrieve_user_handler(token: Token, _: ASGIConnection) -> User | None:
    """Retrieve user based on JWT token."""
    from app.db import sqlalchemy_config

    with sqlalchemy_config.get_session() as session:
        users_repo = UserRepository(session=session)

        # Use get_one_or_none to safely return None if the user is not found,
        # which is more explicit than catching a broad exception.
        return users_repo.get_one_or_none(username=token.sub)


oauth2_auth = OAuth2PasswordBearerAuth[User](
    retrieve_user_handler=retrieve_user_handler,
    token_secret=settings.jwt_secret_key,
    token_url="/auth/login",
    exclude=["/auth/login", "/schema", "/users"],
)
