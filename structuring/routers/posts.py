from typing import List

from fastapi import APIRouter, HTTPException, status

from models.post import Post, PostCreate
from database import database

router = APIRouter()


@router.get("/")
async def all() -> List[Post]:
    return list(database.posts.values())


@router.get("/{id}")
async def get(id: int) -> Post:
    try:
        return database.posts[id]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(post_create: PostCreate) -> Post:
    try:
        database.users[post_create.user]
    except KeyError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"User with id {post_create.user} doesn't exist.",
        )

    new_id = max(database.posts.keys() or (0,)) + 1
    post = Post(id=new_id, **post_create.dict())
    database.posts[new_id] = post
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    try:
        database.posts.pop(id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)