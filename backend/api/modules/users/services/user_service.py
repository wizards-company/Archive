from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from datetime import datetime, timezone
from passlib.context import CryptContext

from api.modules.users.models.User import User
from api.shared.exceptions.user_exceptions import UserNotFoundException, UserAlreadyExistsException
from api.shared.exceptions.database_exceptions import DataBaseTransactionException
from api.modules.users.schemas.user_schema import UserResponsePublic

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def create_user(self, user_data: dict) -> UserResponsePublic:
        """
        Creates a new user in the database.

        Args:
            user_data (dict): The data for the new user.

        Returns:
            User: The created user.

        Raises:
            UserAlreadyExistsException: If a user with the given CPF or email already exists.
            DataBaseTransactionException: If there is an error during the database transaction.
        """
        try:
            await self.get_user_by_cpf(user_data["cpf"])
        except UserNotFoundException:
            pass
        else:
            raise UserAlreadyExistsException("User with this cpf already exists.")
        
        try:
            await self.get_user_by_email(user_data["email"])
        except UserNotFoundException:
            pass
        else:
            raise UserAlreadyExistsException("User with this email already exists.")
        
        hashed_password = pwd_context.hash(user_data["password"])
        user_data["password"] = hashed_password
        new_user = User(**user_data, dateCreated=datetime.now(timezone.utc))
        try:
            self.session.add(new_user)
            await self.session.commit()
            await self.session.refresh(new_user)   

        except:
            await self.session.rollback()
            raise DataBaseTransactionException()
        
        return new_user
            
    async def get_all_users(self, skip: int = 0, limit: int = 10, active: Optional[bool] = None) -> List[UserResponsePublic]:

        query = select(User)
        
        if active is not None:
            query = query.where(User.active.is_(active))
        
        query = query.offset(skip).limit(limit)
        
        result = await self.session.execute(query)
        users = result.scalars().all()
            
        if not users:
            raise UserNotFoundException()
            
        return users
        
    async def get_user_by_id(self, user_id: str) -> UserResponsePublic:
        """
        Retrieves a user by their ID.

        Args:
            ID (str): The ID of the user.

        Returns:
            User: The user with the given ID.

        Raises:
            UserNotFoundException: If no user is found with the given ID.
        """
        stmt = select(User).filter(User.id == user_id)
        result = await self.session.execute(stmt)
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException()
        
        return user
        
    async def get_user_by_cpf(self, cpf: str):
        """
        Retrieves a user by their CPF.

        Args:
            cpf (str): The CPF of the user.

        Returns:
            User: The user with the given CPF.

        Raises:
            UserNotFoundException: If no user is found with the given CPF.
        """
        stmt = select(User).filter(User.cpf == cpf)
        result = await self.session.execute(stmt)
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException()
        
        return user
        
    async def get_user_by_email(self, email: str) -> UserResponsePublic:
        """
        Retrieves a user by their email.

        Args:
            email (str): The email of the user.

        Returns:
            User: The user with the given email.

        Raises:
            UserNotFoundException: If no user is found with the given email.
        """
        stmt = select(User).filter(User.email == email)
        result = await self.session.execute(stmt)
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException()
        
        return user