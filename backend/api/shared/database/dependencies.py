from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from api.shared.database.connection import async_session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

SECRET_KEY = "123"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/")

async def get_db():
    """
    Provides a database session.

    Yields:
        AsyncSession: The database session.
    """
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
            
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
        
async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Retrieves the current user based on the JWT token.

    Args:
        token (str): The JWT token from the Authorization header.

    Returns:
        Dict[str, Union[str, int]]: The payload from the decoded JWT token.

    Raises:
        HTTPException: If the token is invalid, expired, or has invalid claims.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTClaimsError:
        raise HTTPException(status_code=401, detail="Invalid token claims")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
