
import asyncio

from motor import motor_asyncio
from odmantic import AIOEngine
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


MONGO_URI = "mongodb+srv://TROJ3N:Nethika123@cluster0.uppg6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MONGO_PORT = 27017
MONGO_DB = "DaisyX"

# Init MongoDB
mongodb = MongoClient(MONGO_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_URI, MONGO_PORT)
db = motor[MONGO_DB]

engine = AIOEngine(motor, MONGO_DB)
