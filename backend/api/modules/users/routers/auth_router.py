from fastapi import APIRouter, Depends, status

from api.shared.database.dependencies import get_current_user
from api.shared.utils.utils import create_access_token
from api.modules.users.controllers.auth_controller import AuthController
from api.modules.users.schemas.token_schema import TokenRequest, TokenResponse

router = APIRouter()

@router.post("/", response_model=TokenResponse, status_code=status.HTTP_200_OK, summary="User Login", tags=["auth"])
async def authenticate(data: TokenRequest, auth_controller: AuthController = Depends()) -> TokenResponse:
    """
    Authenticate a user and return a JWT token.

    Args:
        user (TokenRequest): The user login credentials.
        db (AsyncSession): The database session.

    Returns:
        TokenResponse: The access token and its type.

    Raises:
        InvalidCredentialsException: If the email or password is incorrect.
    """    
    user_id = await auth_controller.authenticate_user(data.email, data.password)
    access_token = create_access_token(user_id=user_id)
    return TokenResponse(access_token=access_token, token_type="bearer")

@router.get("/", summary="Test Authentication", tags=["auth"])
async def test_authentication(current_user: dict = Depends(get_current_user)):
    """
    Test route to verify JWT authentication.

    Args:
        current_user (dict): The current authenticated user based on the JWT token.

    Returns:
        dict: A message confirming authentication and user information.
    """
    return {"message": "User authenticated", "user": current_user}