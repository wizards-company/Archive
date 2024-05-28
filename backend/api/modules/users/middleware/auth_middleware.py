from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import jwt

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get('Authorization')
        user_info = None
        
        if token:
            try:        
                token = token.split("Bearer ")[-1]
                payload = jwt.decode(token, "123", algorithms=["HS256"])
                user_info = {"user_id": payload["sub"]}
                request.state.user = user_info 

            except jwt.PyJWTError:
                pass

        response = await call_next(request)
        return response