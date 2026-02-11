import db
import jwt

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from sqlmodel import select
from pwdlib import PasswordHash
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone

# The secret key is kept here purely for conveninence and demonstration purposes. Never ever do this.
SECRET_KEY = "b8613fbab7948758b8dd5fc0341b27784433bb2cf1e22a9fa01758b7bc0e5f36"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_user(username:str, session: db.Session):
    user = session.exec(select(db.User).where(db.User.email == username)).first()
    if user:
        return user

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def hash_password(password):
    return password_hash.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(username:str, password:str, session: db.Session):
    user = get_user(username, session)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], session: db.SessionDep):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    user = get_user(username, session)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user
