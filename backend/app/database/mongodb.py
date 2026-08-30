import os

import certifi
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ai_resume_analyzer")

client = MongoClient(
    MONGODB_URI,
    server_api=ServerApi("1"),
    tlsCAFile=certifi.where(),
)

db = client[DATABASE_NAME]
analyses_collection = db["analyses"]


def test_connection():
    client.admin.command("ping")
    return True
