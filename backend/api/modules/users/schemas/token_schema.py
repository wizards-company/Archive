from typing import Annotated

from pydantic import BaseModel, Field, EmailStr, ConfigDict

class TokenRequest(BaseModel):
    email: Annotated[EmailStr, Field(..., max_length=45, description="The user's email address")]
    password: Annotated[str, Field(...,  min_length=8, max_length=255, description="The user's password")]
    
    model_config = ConfigDict(from_attributes=True)
    
class TokenResponse(BaseModel):
    access_token: str = Field(description="The JWT access token")
    token_type: str = Field(description="The type of the token, typically 'bearer'")
    
    model_config = ConfigDict(from_attributes=True)