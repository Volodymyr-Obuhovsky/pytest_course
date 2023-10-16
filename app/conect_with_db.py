from contextlib import contextmanager
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Example synch engine
sync_engine = create_engine(url=settings.DATABASE_URL_psycopg,
                            # "echo=True" - all requests to db will be displayed in terminal
                            # echo=True,
                            # "pool_size" - max quantity db connections during session
                            # pool_size=5,
                            # "max_overflow" - quantity of extra db connections
                            # max_overflow=10
                            )

# Example async engine
# async_engine = create_async_engine(url=settings.DATABASE_URL_asyncpg, echo=True)

SessionLocal = sessionmaker(bind=sync_engine, autoflush=False, autocommit=False)
# SessionLocal = async_sessionmaker(bind=async_engine, autoflush=False, autocommit=False)

Base = declarative_base()
inspector = inspect(sync_engine)


def get_db():
    try:
        yield SessionLocal()
    finally:
        SessionLocal().close()


db_context = contextmanager(get_db)
