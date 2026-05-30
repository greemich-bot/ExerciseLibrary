# client_test.py
import json
import zmq
from config import ZMQ_BIND_ADDRESS


def send_request(socket, payload):
    socket.send_string(json.dumps(payload))
    raw_response = socket.recv_string()
    return json.loads(raw_response)


def print_find_result(title, response):
    print(f"\n--- {title} ---")
    if response.get("status") != "success":
        print("Server Error:", response)
        return

    exercises = response.get("data", [])
    print(f"Matches: {len(exercises)}")
    for exercise in exercises:
        print(f"- {exercise.get('name')} ({exercise.get('muscleGroup')}, {exercise.get('machineType')})")

def run_test():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(ZMQ_BIND_ADDRESS)

    print("--- Testing 'create' action ---")
    create_payload = {
        "action": "create",
        "data": {
            "name": "Barbell Bench Press",
            "muscleGroup": "Chest",
            "machineType": "Barbell",
            "difficulty": "intermediate"
        }
    }
    create_response = send_request(socket, create_payload)
    print("Server Response:", create_response)

    query_examples = [
        {
            "title": "Find chest + barbell",
            "payload": {"action": "find", "muscleGroup": "Chest", "machineType": "Barbell"},
        },
        {
            "title": "Find back + machine",
            "payload": {"action": "find", "muscleGroup": "Back", "machineType": "Machine"},
        },
        {
            "title": "Find shoulders + cable",
            "payload": {"action": "find", "muscleGroup": "Shoulders", "machineType": "Cable"},
        },
        {
            "title": "Find all leg exercises",
            "payload": {"action": "find", "muscleGroup": "Legs"},
        },
        {
            "title": "Find all bodyweight exercises",
            "payload": {"action": "find", "machineType": "Bodyweight"},
        },
        {
            "title": "Find all arm exercises",
            "payload": {"action": "find", "muscleGroup": "Arms"},
        },
    ]

    for query in query_examples:
        response = send_request(socket, query["payload"])
        print_find_result(query["title"], response)

if __name__ == "__main__":
    run_test()
