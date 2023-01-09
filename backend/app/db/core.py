from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/asyncalchemy"

engine = create_async_engine(DATABASE_URL, echo = True)
Base = declarative_base()
async_sess = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
        )


async def get_session() -> AsyncSession:
    async with async_sess() as session:
        yield session
