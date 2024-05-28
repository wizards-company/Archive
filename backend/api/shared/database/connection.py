from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from api.shared.database.database_config import get_database_url
    

DATABASE_URL = get_database_url()
print(f"Using database URL: {DATABASE_URL}")

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
