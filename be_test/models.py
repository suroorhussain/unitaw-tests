from datetime import date
from pydantic import BaseModel, HttpUrl, EmailStr

class Event(BaseModel):
    title: str
    description: str
    location: str
    featured: bool
    image: HttpUrl | None = None
    datelist: list[date]

class EventResponse(Event):
    id: int

class User(BaseModel):
    email: EmailStr

class UserInDB(User):
    hashed_password: str
