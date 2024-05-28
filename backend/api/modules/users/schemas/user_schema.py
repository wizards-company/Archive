import uuid
from typing import Annotated
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime

class UserRequestCreate(BaseModel):
    cpf: Annotated[str, Field(min_length=11, max_length=11, description="CPF must be exactly 11 characters.")]
    email: Annotated[EmailStr, Field(max_length=45, description="Email must be at most 45 characters.")]
    name: Annotated[str, Field(min_length=7, max_length=100, description="Name must be between 7 and 100 characters.")]
    password: Annotated[str, Field(min_length=8, max_length=255, description="Password must be between 8 and 255 characters.")]
    
    model_config = ConfigDict(from_attributes=True)
    
class UserResponsePublic(BaseModel):
    id: Annotated[uuid.UUID, Field()]
    email: Annotated[EmailStr, Field()]
    name: Annotated[str, Field()]
    active: Annotated[bool, Field()]
    dateCreated: Annotated[datetime, Field()]
    dateLogin: Annotated[Optional[datetime], Field()]
    
    model_config = ConfigDict(from_attributes=True)