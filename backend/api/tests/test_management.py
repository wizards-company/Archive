import pytest
import jwt
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_create_book(client: AsyncClient):
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
    access_token = body['access_token']
       
    new_book = {
        "title": "string1",
        "author": "string1",
        "publisher": "string1",
        "page": 100,
        "datePublished": "2024-05-25T12:16:09.362Z"
    }
    
    headers = {"Authorization": f"Bearer {access_token}"}

    response = await client.post("/management/", json=new_book, headers=headers)
    assert response.status_code == status.HTTP_201_CREATED
