from uuid import UUID
from fastapi import APIRouter, Depends, status, HTTPException, Request

from api.modules.users.controllers.management_controller import ManagementController
from api.modules.books.schemas.book_schema import BookResponsePublic, BookRequestCreate

router = APIRouter()

@router.post("/", response_model=BookResponsePublic, status_code=status.HTTP_201_CREATED, summary="Create a new book", tags=["management"])
async def create_book(request: Request, 
                      data_book: BookRequestCreate, 
                      book_controller:ManagementController = Depends()
                      ) -> BookResponsePublic:
    
    print(request.state)
    if not hasattr(request.state, "user"):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    new_book = await book_controller.create_new_book(data_book.model_dump())
    
    return new_book