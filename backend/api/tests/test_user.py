import pytest
import uuid
from sqlalchemy.dialects.postgresql import UUID
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_find_all_users_not_found(client: AsyncClient) -> None:
    """
    Test the behavior when no users are found.

    This test checks that the endpoint returns a 404 status code
    and the correct error message when no users are found.
    """
    response = await client.get("/users/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}
    
@pytest.mark.asyncio
async def test_find_user_by_id_not_found(client: AsyncClient) -> None:
    """
    Test the behavior when no user by ID are found.

    This test checks that the endpoint returns a 404 status code
    and the correct error message when no user are found.
    """  
    non_existent_id = "2CA263F1-5C94-11E0-84CC-002170FBAC5B"
    response = await client.get(f"/users/{non_existent_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "User not found"}

@pytest.mark.asyncio
async def test_find_all_users_pagination(client: AsyncClient) -> None:
    """
    Test the retrieval of all users with pagination.

    This test checks that the endpoint returns a 200 status code
    and the correct list of users on pagination.
    """
    user1 = {
        "email": "user1@example.com",
        "cpf": "12345678911",
        "password": "securepassword",
        "name": "UserExample1",
        "active": True
    }
    
    user2 = {
        "email": "user2@example.com",
        "cpf": "12345678912",
        "password": "securepassword",
        "name": "UserExample2",
        "active": True
    }
    
    user3 = {
        "email": "user3@example.com",
        "cpf": "12345678913",
        "password": "securepassword",
        "name": "UserExample3",
        "active": True
    }
    
    response1 = await client.post("/users/", json=user1)
    assert response1.status_code == status.HTTP_201_CREATED
    response2 = await client.post("/users/", json=user2)
    assert response2.status_code == status.HTTP_201_CREATED
    response3 = await client.post("/users/", json=user3)
    assert response3.status_code == status.HTTP_201_CREATED
    
    response = await client.get("/users/?skip=0&limit=2")
    assert response.status_code == status.HTTP_200_OK

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 2

    emails = [user["email"] for user in body]
    assert user1["email"] in emails
    assert user2["email"] in emails

@pytest.mark.asyncio
async def test_find_user_by_id(client: AsyncClient) -> None:
    """
    Test the retrieval of user by id.

    This test checks that the endpoint returns a 200 status code
    and the correct user.
    """
    user = {
        "email": "user@example.com",
        "cpf": "12345678911",
        "password": "securepassword",
        "name": "UserExample",
        "active": True
    }
        
    response = await client.post("/users/", json=user)
    assert response.status_code == status.HTTP_201_CREATED
    
    body = response.json()
    user_id = body["id"]
    
    response = await client.get(f"/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK

    body = response.json()
    assert body["email"] == user["email"]
    assert body["name"]  == user["name"]

@pytest.mark.asyncio
async def test_find_all_users(client: AsyncClient) -> None:
    """
    Test the retrieval of all users.

    This test checks that the endpoint returns a 200 status code
    and the correct list of users.
    """
    user1 = {
        "email": "user1@example.com",
        "cpf": "12345678911",
        "password": "securepassword",
        "name": "UserExample1",
        "active": True
    }
    
    user2 = {
        "email": "user2@example.com",
        "cpf": "12345678912",
        "password": "securepassword",
        "name": "UserExample2",
        "active": True
    }
    
    response1 = await client.post("/users/", json=user1)
    assert response1.status_code == status.HTTP_201_CREATED
    response2 = await client.post("/users/", json=user2)
    assert response2.status_code == status.HTTP_201_CREATED
    
    response = await client.get("/users/")
    assert response.status_code == status.HTTP_200_OK

    body = response.json()
    assert isinstance(body, list)
    assert len(body) == 2

    emails = [user["email"] for user in body]
    assert user1["email"] in emails
    assert user2["email"] in emails
 
@pytest.mark.asyncio
async def test_create_new_user_duplicate_email(client: AsyncClient) -> None:
    """
    Test the creation of a user with a duplicate email.

    This test checks that creating a user with an existing email
    returns a 409 status code and the correct error message.
    """
    user = {
        "email": "user@example.com",
        "cpf": "12345678911",
        "password": "securepassword",
        "name": "UserExample",
        "active": True
    }
    
    new_user = {
        "email": "user@example.com",
        "cpf": "12345678912",
        "password": "securepassword",
        "name": "New User",
        "active": True
    }
    
    response1 = await client.post("/users/", json=user)
    assert response1.status_code == status.HTTP_201_CREATED
    
    response = await client.post("/users/", json=new_user)
    assert response.status_code == status.HTTP_409_CONFLICT
    
    body = response.json()
    assert body["detail"] == "User with this email already exists."
 
@pytest.mark.asyncio
async def test_create_new_user_duplicate_cpf(client: AsyncClient) -> None:
    """
    Test the creation of a user with a duplicate cpf.

    This test checks that creating a user with an existing cpf
    returns a 409 status code and the correct error message.
    """
    user = {
        "email": "user@example.com",
        "cpf": "12345678911",
        "password": "securepassword",
        "name": "UserExample",
        "active": True
    }
    
    new_user = {
        "email": "use2@example.com",
        "cpf": "12345678911",
        "password": "securepassword",
        "name": "New User",
        "active": True
    }
    
    response1 = await client.post("/users/", json=user)
    assert response1.status_code == status.HTTP_201_CREATED
    
    response = await client.post("/users/", json=new_user)
    assert response.status_code == status.HTTP_409_CONFLICT
    
    body = response.json()
    assert body["detail"] == "User with this cpf already exists."

@pytest.mark.asyncio
async def test_create_new_user(client: AsyncClient) -> None:
    """
    Test the creation of a new user.

    This test checks that a new user can be successfully created,
    and that the response contains the correct user data.
    """
    new_user = {
        "email": "newuser@example.com",
        "cpf": "12345678911",
        "password": "securepassword",
        "name": "New User",
        "active": True
    }

    response = await client.post("/users/", json=new_user)
    assert response.status_code == status.HTTP_201_CREATED
    
    body = response.json()
    assert body["email"] == new_user["email"]
    assert body["name"] == new_user["name"]
    assert body["active"] == new_user["active"]