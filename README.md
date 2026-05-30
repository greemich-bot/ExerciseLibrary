# Exercise Library Microservice
A micro service that stores exercises by muscle group and equipment.

# Setup
The Microservice stores exercises in MongoDB, so you will need to create a new cluster and use seed.py to populate. Create a .env file to store your connection string. Config.py houses other connection info for mongoDB and ZeroMQ.

# Connecting and Sending/Receiving

Server.py supports create and read operations using "create" and "find".

1. To create exercises use "create":
    {
        "action": "create",
        "data": {
            "name": "Barbell Bench Press",
            "muscleGroup": "Chest",
            "machineType": "Barbell",
            "difficulty": "intermediate"
        }
    }

2. To query use "find" with "muscleGroup" and/or "machineType":

    {
        "action": "find", "muscleGroup": "Chest", "machineType": "Barbell"
    }

3. Supported muscle groups: Chest, Back, Arms, Shoulders, Legs
4. Supported machine types: Machine, Cable, Dumbbell, Barbell, Bodyweight
    
