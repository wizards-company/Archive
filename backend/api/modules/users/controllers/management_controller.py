from uuid import UUID
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.modules.books.services.book_service import BookService
from api.modules.books.schemas.book_schema import BookResponsePublic
from api.shared.database.dependencies import get_db
from api.shared.database.dependencies import get_current_user

class ManagementController:
    def __init__(self, session: AsyncSession = Depends(get_db), user_id: UUID = Depends(get_current_user)):
        self.session = session
        self.user_id = user_id
        self.book_service = BookService(session)
        
    async def create_new_book(self, data_book) -> BookResponsePublic:
        if not self.user_id:
            raise HTTPException(status_code=401, detail="Authentication required")
        new_book = await self.book_service.create_book(self.user_id, data_book)
        
        return new_book