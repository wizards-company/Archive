import os

def get_database_url():
    return os.getenv("DATABASE_URL", "sqlite+aiosqlite:///.sqlite")

"""
from dotenv import load_dotenv

def get_database_url():
    env = os.getenv("ENV")
    if env == "production":
        load_dotenv(".env.prod")
    elif env == "development":
        load_dotenv(".env.dev")
    elif env == "test":
        load_dotenv(".env.test")
    else:
        return "sqlite+aiosqlite:///.sqlite"
        

    return os.getenv("DATABASE_URL")
"""