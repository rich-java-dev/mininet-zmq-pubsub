import time
import zmq
import sys

context = zmq.Context()

socket = context.socket(zmq.SUB)

topic = sys.argv[2] if len(sys.argv) > 2 else ''
proxy = sys.argv[1] if len(sys.argv) > 1 else "10.0.0.1"

port = "5556"
socket.connect(f'tcp://{proxy}:{port}')
socket.setsockopt_string(zmq.SUBSCRIBE, topic)

print(f"Subscriber listening to '{proxy}' w/ topic '{topic}'")

while True:
    msg = socket.recv_string()
    print(msg)
    time.sleep(0.1)
