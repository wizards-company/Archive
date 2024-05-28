from uuid import UUID
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.modules.books.services.book_service import BookService
from api.modules.books.schemas.book_schema import BookResponsePublic
from api.shared.database.dependencies import get_db

class BookController:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.session = session
        self.book_service = BookService(session)
           
    async def get_all_books(self, skip: int = 0, limit: int = 10) -> List[BookResponsePublic]:
        books = await self.book_service.get_all_books(skip=skip, limit=limit)

        return books