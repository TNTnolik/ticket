from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from db.service import init_models, get_session, get_tickets, add_ticket
from db.schemas import Ticket


app = FastAPI()


@app.get("/tickets", response_model=list[Ticket])
async def r_get_tickets(session: AsyncSession = Depends(get_session)):
    tickets = await get_tickets(session)
    return [Ticket(title=t.title, description=t.description) for t in tickets]


@app.post("/tickets/add")
async def r_add_ticket(ticket: Ticket, session: AsyncSession = Depends(get_session)):
    new_ticket = add_ticket(session = session, title = ticket.title, description = ticket.description)
    try:
        await session.commit()
        return new_ticket
    except IntegrityError as ex:
        await session.rollback()


