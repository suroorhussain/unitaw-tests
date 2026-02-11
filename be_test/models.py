from datetime import date
from pydantic import BaseModel, HttpUrl

class Event(BaseModel):
    title: str
    description: str
    location: str
    featured: bool
    image: HttpUrl | None = None
    datelist: list[date]

class EventResponse(Event):
    id: int
