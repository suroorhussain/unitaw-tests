import datetime
from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Field, Session, select, create_engine

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

class EventBase(SQLModel):
    title: str
    description: str
    location: str
    featured: bool
    image: str | None = None
    date: datetime.date
    price: float

class Event(EventBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class EventDetail(EventBase):
    id: int

class UserBase(SQLModel):
    email: str

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str

class UserCreate(UserBase):
    password: str
    