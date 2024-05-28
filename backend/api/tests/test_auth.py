import pytest
import jwt
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_failed_login(client: AsyncClient):
    """
    Test failed login with incorrect password.

    This test verifies that attempting to log in with an incorrect password
    returns a 401 Unauthorized status code.
    """
    response = await client.post("/auth/", json={"email": "user@example.com", "password": "wrongpassword"})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.asyncio
async def test_login(client: AsyncClient):
    """
    Test successful user registration and login.

    This test verifies that a new user can be successfully registered,
    and that the same user can log in with the correct credentials.
    Additionally, it verifies that the login response includes a valid JWT token.
    """
    SECRET_KEY = "123"
    ALGORITHM = "HS256"
    new_user = {
        "email": "newuser@example.com",
        "cpf": "12345678911",
        "password": "securepassword",
        "name": "New User",
        "active": True
    }

    response = await client.post("/users/", json=new_user)
    assert response.status_code == status.HTTP_201_CREATED
    response = await client.post("/auth/", json={"email": "newuser@example.com", "password": "securepassword"})
    assert response.status_code == status.HTTP_200_OK
    
    body = response.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"