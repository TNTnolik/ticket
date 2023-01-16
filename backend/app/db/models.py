from sqlalchemy import Column, DateTime, ForeignKey, String, Integer, Text, Boolean
from sqlalchemy.orm import relationship
from .core import Base
import datetime
from passlib.hash import bcrypt


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hash_password = Column(String)
    tg_id = Column(Integer, unique=True, nullable=True)
    tg_auth = Column(String, unique=True, nullable=True)
    rank_id = Column(Integer, ForeignKey("ranks.id"), nullable=True)
    date_create = Column(DateTime, default=datetime.datetime.utcnow)

    rank = relationship("Rank", back_populates="user")
    own_tickets = relationship("Ticket", back_populates="owner")
    work_tickets = relationship("Ticket", back_populates="worker")
    
    def verify_password(self, password:str):
        return bcrypt.verify(password, self.hash_password)

class Rank(Base):
    __tablename__ = "ranks"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    level = Column(Integer)

    user = relationship("User", back_populates="rank")


class Adress(Base):
    __tablename__ = "adress"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)

    ticket = relationship("Ticket", back_populates="adress")


class Type(Base):
    __tablename__ = "types"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(Text)

    ticket = relationship("Ticket", back_populates="type")


class State(Base):
    __tablename__ = "stats"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    default = Column(Boolean)

    ticket = relationship("Ticket", back_populates="state")

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type_id = Column(Integer, ForeignKey("types.id"), nullable=False)
    adress_id = Column(Integer, ForeignKey("adress.id"), nullable=False)
    worker_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    state_id = Column(Integer, ForeignKey("stats.id"), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_last_updated = Column(DateTime, default=datetime.datetime.utcnow)
    
    owner = relationship("User", back_populates="own_tickets")
    worker = relationship("User", back_populates="work_tickets")
    type = relationship("Type", back_populates="ticket")
    adress = relationship("Adress", back_populates="ticket")
    state = relationship("State", back_populates="ticket")

