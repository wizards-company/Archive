from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, Depends, Query, status

from api.modules.books.controllers.book_controller import BookController
from api.modules.books.schemas.book_schema import BookResponsePublic

router = APIRouter()

@router.get("/", response_model=List[BookResponsePublic], status_code=status.HTTP_200_OK, summary="Get a list of books", tags=["books"])
async def find_all_books(skip: int = Query(0, description="Number of records to skip for pagination"),
                         limit: int = Query(10, description="Maximum number of records to return"),
                         book_controller: BookController = Depends()
                        ) -> List[BookResponsePublic]:
    
    """Retrieve a list of books with pagination.

    Args:
        
        skip (int, optional): Number of records to skip for pagination.
        limit (int, optional): Maximum number of records to return.
        book_controller (bookController, optional): The book controller. Defaults to Depends().

    Returns:
        List[BookResponsePublic]: The list of books.
        
    Raises:
        HTTPException: If no book are found.
    """
    
    books = await book_controller.get_all_books(skip=skip, limit=limit)
    return [BookResponsePublic.model_validate(book.__dict__) for book in books]

