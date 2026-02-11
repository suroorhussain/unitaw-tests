from sqlmodel import select
import auth
import db

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated    

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
async def create_event(event: db.EventBase, current_user: Annotated[db.UserBase, Depends(auth.get_current_user)], session: db.SessionDep) -> db.EventDetail:
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
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: db.SessionDep):
    user = auth.authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.email})
    return auth.Token(access_token=access_token, token_type="bearer")

@app.post("/register")
async def register(user: db.UserCreate, session: db.SessionDep) -> db.UserBase:
    existing_user = auth.get_user(user.email, session)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = db.User(email=user.email, hashed_password=auth.hash_password(user.password))
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user