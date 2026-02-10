from pydantic import BaseModel

class Event(BaseModel):
    title: str
    description: str
    location: str
    featured: bool
    image: str
    datelist: list[str]
