import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import create_engine
from sqlalchemy import pool

from alembic import context

from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

env = os.getenv("ENV", "development")
if env == "production":
    load_dotenv(".env.prod")
elif env == "testing":
    load_dotenv(".env.test")
else:
    load_dotenv(".env.dev")

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from api.shared.database.connection import Base 
from api.modules.users.models.User import User
from api.modules.books.models.Book import Book

target_metadata = None

from api.shared.database.connection import Base, DATABASE_URL

config.set_main_option('sqlalchemy.url', DATABASE_URL)

# Alterar a URL para usar o driver síncrono
SYNC_DATABASE_URL = DATABASE_URL.replace("asyncpg", "psycopg2")

# set the URL dynamically from the SYNC_DATABASE_URL
config.set_main_option('sqlalchemy.url', SYNC_DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()