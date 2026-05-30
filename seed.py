from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME
from database import ExerciseDB


exercises_data = [
    # --- CHEST ---
    {"name": "Barbell Bench Press", "muscleGroup": "chest", "machineType": "barbell", "difficulty": "intermediate"},
    {"name": "Incline Dumbbell Press", "muscleGroup": "chest", "machineType": "dumbbell", "difficulty": "intermediate"},
    {"name": "Cable Crossover", "muscleGroup": "chest", "machineType": "cable", "difficulty": "intermediate"},
    {"name": "Chest Fly Machine", "muscleGroup": "chest", "machineType": "machine", "difficulty": "beginner"},
    {"name": "Push-Up", "muscleGroup": "chest", "machineType": "bodyweight", "difficulty": "beginner"},

    # --- BACK ---
    {"name": "Barbell Deadlift", "muscleGroup": "back", "machineType": "barbell", "difficulty": "advanced"},
    {"name": "Lat Pulldown", "muscleGroup": "back", "machineType": "machine", "difficulty": "beginner"},
    {"name": "One-Arm Dumbbell Row", "muscleGroup": "back", "machineType": "dumbbell", "difficulty": "intermediate"},
    {"name": "Seated Cable Row", "muscleGroup": "back", "machineType": "cable", "difficulty": "beginner"},
    {"name": "Pull-Up", "muscleGroup": "back", "machineType": "bodyweight", "difficulty": "intermediate"},

    # --- LEGS ---
    {"name": "Barbell Back Squat", "muscleGroup": "legs", "machineType": "barbell", "difficulty": "advanced"},
    {"name": "Dumbbell Bulgarian Split Squat", "muscleGroup": "legs", "machineType": "dumbbell", "difficulty": "advanced"},
    {"name": "Leg Press", "muscleGroup": "legs", "machineType": "machine", "difficulty": "beginner"},
    {"name": "Lying Leg Curl", "muscleGroup": "legs", "machineType": "machine", "difficulty": "beginner"},
    {"name": "Bodyweight Calf Raise", "muscleGroup": "legs", "machineType": "bodyweight", "difficulty": "beginner"},

    # --- SHOULDERS ---
    {"name": "Overhead Barbell Press", "muscleGroup": "shoulders", "machineType": "barbell", "difficulty": "intermediate"},
    {"name": "Dumbbell Lateral Raise", "muscleGroup": "shoulders", "machineType": "dumbbell", "difficulty": "beginner"},
    {"name": "Cable Face Pull", "muscleGroup": "shoulders", "machineType": "cable", "difficulty": "intermediate"},
    {"name": "Shoulder Press Machine", "muscleGroup": "shoulders", "machineType": "machine", "difficulty": "beginner"},
    {"name": "Pike Push-Up", "muscleGroup": "shoulders", "machineType": "bodyweight", "difficulty": "intermediate"},

    # --- ARMS ---
    {"name": "Barbell Bicep Curl", "muscleGroup": "arms", "machineType": "barbell", "difficulty": "beginner"},
    {"name": "Dumbbell Hammer Curl", "muscleGroup": "arms", "machineType": "dumbbell", "difficulty": "beginner"},
    {"name": "Cable Tricep Pushdown", "muscleGroup": "arms", "machineType": "cable", "difficulty": "beginner"},
    {"name": "Tricep Extension Machine", "muscleGroup": "arms", "machineType": "machine", "difficulty": "beginner"},
    {"name": "Diamond Push-Up", "muscleGroup": "arms", "machineType": "bodyweight", "difficulty": "intermediate"}
]

def seed_database():
    db = ExerciseDB()
    
    # Clear existing data to prevent duplicates
    db.collection.delete_many({})
    
    # Insert seed data
    db.collection.insert_many(exercises_data)
    print("Database seeded with initial exercise data.")

if __name__ == "__main__":
    seed_database()