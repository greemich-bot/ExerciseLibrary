# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Your live MongoDB Atlas connection string
MONGO_URI = os.getenv("MONGO_URI")

# Database and collection names
DB_NAME = "ExerciseLib"
COLLECTION_NAME = "exercises"

# ZeroMQ internal networking configuration
ZMQ_BIND_ADDRESS = "tcp://127.0.0.1:5555"
