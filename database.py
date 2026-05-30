# database.py
import certifi
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

class ExerciseDB:
    def __init__(self):
        self.client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
        self.db = self.client[DB_NAME]
        self.collection = self.db[COLLECTION_NAME]
        
        # Ensure fast lookups by indexing muscleGroup and machineType
        self.collection.create_index([("muscleGroup", 1), ("machineType", 1)])

    def create_exercise(self, data):
        """Inserts an exercise into MongoDB."""
        # Normalize casing for reliable querying
        data["muscleGroup"] = data.get("muscleGroup", "").strip().lower()
        data["machineType"] = data.get("machineType", "").strip().lower()
        
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def find_exercises(self, muscle_group=None, machine_type=None):
        """Filters exercises by muscle group and/or machine type."""
        query = {}
        if muscle_group:
            query["muscleGroup"] = muscle_group.strip().lower()
        if machine_type:
            query["machineType"] = machine_type.strip().lower()

        results = list(self.collection.find(query))
        
        # Convert ObjectId to string for JSON compliance
        for doc in results:
            doc["_id"] = str(doc["_id"])
            
        return results
