from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .core import Base, engine, async_sess
from .models import *


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_sess() as session:
        yield session


async def get_tickets(session: AsyncSession) -> list[Ticket]:
    result = await session.execute(select(Ticket).limit(20))
    return result.scalars().all()


def add_ticket(session: AsyncSession, title:str, description:str):
    new_ticket = Ticket(title=title, description=description)
    session.add(new_ticket)
    return new_ticket
