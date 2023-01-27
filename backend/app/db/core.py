from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres:password@db/postgres_db"

engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_sess = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)
