from typing import List

from fastapi import APIRouter, HTTPException, status

from models.user import User, UserCreate
from database import database

router = APIRouter()


@router.get("/")
async def all() -> List[User]:
    return list(database.users.values())


@router.get("/{id}")
async def get(id: int) -> User:
    try:
        return database.users[id]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user_create: UserCreate) -> User:
    new_id = max(database.users.keys() or (0,)) + 1
    user = User(id=new_id, **user_create.dict())
    database.users[new_id] = user
    return user


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    try:
        database.users.pop(id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
