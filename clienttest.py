# client_test.py
import json
import zmq
from config import ZMQ_BIND_ADDRESS

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
    socket.send_string(json.dumps(create_payload))
    print("Server Response:", socket.recv_string())

    print("\n--- Testing 'find' action ---")
    find_payload = {
        "action": "find",
        "muscleGroup": "Chest",
        "machineType": "Barbell"
    }
    socket.send_string(json.dumps(find_payload))
    print("Server Response:", socket.recv_string())

if __name__ == "__main__":
    run_test()
