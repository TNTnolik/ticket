from sqlalchemy import Column, String, Integer, Text
from .core import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
