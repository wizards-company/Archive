import uuid
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime, timezone

from api.modules.books.models.Book import Book
from api.shared.exceptions.database_exceptions import DataBaseTransactionException
from api.modules.books.schemas.book_schema import BookResponsePublic
from api.modules.users.services.user_service import UserService
from api.shared.utils.utils import get_user_id_from_token
from api.shared.exceptions.user_exceptions import UserNotFoundException
from api.shared.exceptions.book_exceptions import BookNotFoundException

class BookService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.user_service = UserService(session)
        
    async def create_book(self, token: dict, book_data: dict) -> BookResponsePublic:
        """
        Creates a new book in the database.

        Args:
            user_id (uuid): ID the user book.
            book_data (dict): The data for the new book.

        Returns:
            Book: The created book.

        Raises:
            UserNotFoundException: If not find user.
            DataBaseTransactionException: If there is an error during the database transaction.
        """
        
        try:
            user_id = get_user_id_from_token(token) 
            await self.user_service.get_user_by_id(user_id=user_id)
        except UserNotFoundException:
            UserNotFoundException()
            
        print("id retornado:", user_id)
        new_book = Book(userId=user_id, **book_data, dateCreated=datetime.now(timezone.utc))
        try:
            self.session.add(new_book)
            await self.session.commit()
            await self.session.refresh(new_book)
        except:
            await self.session.rollback()
            raise DataBaseTransactionException()
        
        return new_book
    
    async def get_all_books(self, skip: int = 0, limit: int = 10) -> List[BookResponsePublic]:

        query = select(Book)
        
        query = query.offset(skip).limit(limit)
        
        result = await self.session.execute(query)
        books = result.scalars().all()
            
        if not books:
            raise BookNotFoundException()
            
        return books