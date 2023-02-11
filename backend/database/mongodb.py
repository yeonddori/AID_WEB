from core import settings
from pymongo import MongoClient

client = MongoClient(
    f"mongodb://{settings.mongo_user}:"
    f"{settings.mongo_password}@"
    f"{settings.mongo_host}:"
    f"{settings.mongo_port}/?authMechanism=DEFAULT"
)
db = client["AID_test"]