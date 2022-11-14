from typing import Dict

from models.user import User
from models.post import Post


class DummyDatabase:
    users: Dict[int, User] = {}
    posts: Dict[int, Post] = {}


db = DummyDatabase()
