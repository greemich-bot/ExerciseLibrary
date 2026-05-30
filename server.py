# server.py
import json
import zmq
from config import ZMQ_BIND_ADDRESS
from database import ExerciseDB

def start_server():
    db = ExerciseDB()
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(ZMQ_BIND_ADDRESS)
    
    print(f"Exercise Microservice listening on {ZMQ_BIND_ADDRESS}...")

    while True:
        # 1. Receive incoming request string
        message = socket.recv_string()
        
        try:
            request = json.loads(message)
            action = request.get("action")
            response_payload = {}

            # 2. Route payload based on action type
            if action == "create":
                exercise_data = request.get("data", {})
                new_id = db.create_exercise(exercise_data)
                response_payload = {"id": new_id, "status": "created"}

            elif action == "find":
                muscle = request.get("muscleGroup")
                machine = request.get("machineType")
                exercises = db.find_exercises(muscle_group=muscle, machine_type=machine)
                response_payload = exercises

            else:
                response_payload = {"error": f"Unknown action: '{action}'"}

            # 3. Reply back to client
            socket.send_string(json.dumps({"status": "success", "data": response_payload}))

        except Exception as e:
            # Prevent microservice from crashing by catching and replying with errors
            socket.send_string(json.dumps({"status": "error", "message": str(e)}))

if __name__ == "__main__":
    start_server()
