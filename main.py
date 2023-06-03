from uuid import uuid4, UUID

from fastapi import FastAPI
from typing import List

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="IM",
        last_name="SOKKHORN",
        gender="male",
        roles=["admin"],
    ),
    User(
        id=uuid4(),
        first_name="IM",
        last_name="SOKCOIN",
        gender="male",
        roles=["admin", "user"],
    ),
    User(
        id=uuid4(),
        first_name="Coin",
        last_name="GOGO",
        gender="male",
        roles=["admin", "student"],
    )
]


@app.get("/")
def root():
    return {"HellO": "Khorn"}


@app.get("/api/users")
async def fetch_users():
    return db


@app.post("/api/users/login")
async def login_users(user_first_name: str, user_last_name: str):
    for user in db:
        if user.first_name == user_first_name and user.last_name == user_last_name:
            return user
        else:
            return {"Not User"}


@app.post("/api/users")
async def register_users(user: User):
    db.append(user)
    return {"Register Success"}


@app.delete("/api/users")
async def delete_users(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"Delete User Success"}
    else:
        return {"Not User"}


@app.post("/api/users/searchUser")
async def search_users(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
        else:
            return {"Not User"}
