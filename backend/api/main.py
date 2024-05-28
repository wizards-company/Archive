from fastapi import FastAPI

from api.modules.users.middleware.auth_middleware import AuthMiddleware
from api.modules.users.routers.user_router        import router as user_router
from api.modules.users.routers.auth_router        import router as auth_router
from api.modules.users.routers.management_router  import router as management_router
from api.modules.books.routers.book_router        import router as book_router

app = FastAPI(tittle="Book Trade")

app.add_middleware(AuthMiddleware)

app.include_router(user_router, prefix="/users")
app.include_router(auth_router, prefix="/auth")
app.include_router(management_router, prefix="/management")
app.include_router(book_router, prefix="/books")

@app.get("/")
async def read_root():
    return {"message": "Welcome the Web Book Trade"}

if __name__ == 'main':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)