from typing import Annotated

from ..models import user

from fastapi import APIRouter
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_decode_token(token):
    return user.User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

@router.get("/users/me")
async def read_users_me(current_user: Annotated[user.User, Depends(get_current_user)]):
    return current_user