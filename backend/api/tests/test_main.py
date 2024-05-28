import pytest

@pytest.mark.asyncio
async def test_async_client(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome the Web Book Trade"}
