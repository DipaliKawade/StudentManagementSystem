import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise ValueError("MONGO_URL is not set")

ConnectionString = MongoClient(MONGO_URL)

Database = ConnectionString["Student123"]
collection = Database["StudentInfo"]