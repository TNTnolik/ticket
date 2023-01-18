from fastapi import Depends, FastAPI
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from db.schemas import Ticket
from db.service import add_ticket, get_session, get_tickets


app = FastAPI()


@app.get("/tickets", response_model=list[Ticket])
async def r_get_tickets(session: AsyncSession = Depends(get_session)):
    """Get tickets"""
    tickets = await get_tickets(session)
    return [Ticket(title=t.title, description=t.description) for t in tickets]


@app.post("/tickets/add")
async def r_add_ticket(ticket: Ticket, session: AsyncSession = Depends(get_session)):
    """Create ticket"""
    new_ticket = add_ticket(
        session=session, title=ticket.title, description=ticket.description)
    try:
        await session.commit()
        return new_ticket
    except IntegrityError as ex:
        await session.rollback()
