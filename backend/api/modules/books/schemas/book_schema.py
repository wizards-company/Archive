import uuid
from typing import Annotated, Optional
from pydantic import BaseModel, Field, UUID4, ConfigDict
from datetime import datetime

class BookRequestCreate(BaseModel):
    title: Annotated[str, Field(max_length=100, description="Title of the book.")]
    author: Annotated[str, Field(max_length=100, description="Author of the book.")]
    publisher: Annotated[Optional[str], Field(max_length=100, description="Publisher of the book.")]
    page: Annotated[Optional[int], Field(ge=1, description="Number of pages in the book.")]
    datePublished: Annotated[Optional[datetime], Field(description="Publication date of the book.")]

    model_config = ConfigDict(from_attributes=True)

class BookResponsePublic(BaseModel):
    userId: Annotated[UUID4, Field(description="The UUID of the user who owns the book.")]
    id: Annotated[int, Field(description="The ID of the book, auto-incremented.")]    
    title: Annotated[str, Field()]
    author: Annotated[str, Field()]
    publisher: Annotated[Optional[str], Field()]
    page: Annotated[Optional[int], Field()]
    datePublished: Annotated[Optional[datetime], Field()]
    dateCreated: Annotated[datetime, Field(description="Date when the book was added to the database.")]

    model_config = ConfigDict(from_attributes=True)
