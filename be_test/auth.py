
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from models import User


fake_users_db = {
    "johndoe@example.com": {
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice@example.com": {
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}
def get_user(username:str):
    return fake_users_db.get(username)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def decode_token(token):
    return User(email = token)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = decode_token(token)
    return user

def fake_hash_password(password: str):
    return "fakehashed" + password
