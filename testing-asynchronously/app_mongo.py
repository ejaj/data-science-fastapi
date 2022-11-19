from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

app = FastAPI()
motor_client = AsyncIOMotorClient(
    "mongodb://localhost:27017"
)  # Connection to the whole server
database = motor_client["db-as-orm"]  # Single database instance


def get_database() -> AsyncIOMotorDatabase:
    return database
