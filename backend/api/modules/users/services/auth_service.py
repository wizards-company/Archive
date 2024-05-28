from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext

from api.modules.users.models.User import User
from api.shared.exceptions.auth_exceptions import InvalidCredentialsException

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def authenticate_user(self, email: str, password: str):
        """
        Authenticates a user by email and password.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Raises:
            InvalidCredentialsException: If the credentials are invalid.
        """
        try:
            stmt = select(User).filter(User.email == email)
            result = await self.session.execute(stmt)
            user = result.scalars().first()
            
            if user is None or not pwd_context.verify(password, user.password):
                raise InvalidCredentialsException
            
        except InvalidCredentialsException:
            raise InvalidCredentialsException
        
        return user.id
        
            
