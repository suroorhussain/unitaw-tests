from sqlmodel import select
import auth
import db

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models import Event, EventResponse, User, UserInDB
from typing import Annotated    

EVENTS = [
    {"id": 1, "title": "Event 1", "description": "Description of Event 1", "location": "Location 1", "featured": True, "image": "https://example.com/event1.jpg", "datelist": ["2024-07-01", "2024-07-02"]},
    {"id": 2, "title": "Event 2", "description": "Description of Event 2", "location": "Location 2", "featured": False, "image": "https://example.com/event2.jpg", "datelist": ["2024-08-01", "2024-08-02"]},
    {"id": 3, "title": "Event 3", "description": "Description of Event 3", "location": "Location 3", "featured": True, "image": "https://example.com/event3.jpg", "datelist": ["2024-09-01", "2024-09-02"]},
    {"id": 4, "title": "Event 4", "description": "Description of Event 4", "location": "Location 4", "featured": False, "image": "https://example.com/event4.jpg", "datelist": ["2024-10-01", "2024-10-02"]},
    {"id": 5, "title": "Event 5", "description": "Description of Event 5", "location": "Location 5", "featured": True, "image": "https://example.com/event5.jpg", "datelist": ["2024-11-01", "2024-11-02"]},
    {"id": 6, "title": "Event 6", "description": "Description of Event 6", "location": "Location 6", "featured": False, "image": "https://example.com/event6.jpg", "datelist": ["2024-12-01", "2024-12-02"]},
    {"id": 7, "title": "Event 7", "description": "Description of Event 7", "location": "Location 7", "featured": True, "image": "https://example.com/event7.jpg", "datelist": ["2025-01-01", "2025-01-02"]},
]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    db.create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello world!"}

@app.get("/events")
async def get_events(session: db.SessionDep, limit: int|None = 10, offset: int|None = 0) -> list[db.EventDetail]:
    events = session.exec(select(db.Event).offset(offset).limit(limit)).all()
    return events

@app.post("/events")
async def create_event(event: db.EventBase, current_user: Annotated[User, Depends(auth.get_current_user)], session: db.SessionDep) -> db.EventDetail:
    db_event = db.Event.model_validate(event)
    session.add(db_event)
    session.commit()
    session.refresh(db_event)
    return db_event

@app.get("/events/{event_id}")
async def get_event(event_id: int, session: db.SessionDep) -> db.EventDetail:
    event = session.get(db.Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = auth.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.email})
    return auth.Token(access_token=access_token, token_type="bearer")