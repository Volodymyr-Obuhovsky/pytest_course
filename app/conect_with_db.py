from contextlib import contextmanager
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

engine = create_engine(url=settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
inspector = inspect(engine)


def get_db():
    try:
        yield SessionLocal()
    finally:
        SessionLocal().close()


db_context = contextmanager(get_db)
