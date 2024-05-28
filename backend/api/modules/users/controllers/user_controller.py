from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from api.modules.users.services.user_service import UserService
from api.shared.database.dependencies import get_db
from api.modules.users.schemas.user_schema import UserResponsePublic

class UserController:
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.user_service = UserService(session)
        
    async def create_new_user(self, user_data: dict) -> UserResponsePublic:
        new_user = await self.user_service.create_user(user_data)
        
        return new_user
    
    async def get_user_by_id(self, user_id: str) -> UserResponsePublic:
        user = await self.user_service.get_user_by_id(user_id)
        
        return user
    
    async def get_user_by_email(self, user_email: str) -> UserResponsePublic:
        user = await self.user_service.get_user_by_email(user_email)
        
        return user
        
    async def get_all_users(self, skip: int = 0, limit: int = 10, active: Optional[bool] = None) -> List[UserResponsePublic]:
        users = await self.user_service.get_all_users(skip=skip, limit=limit, active=active)

        return users

