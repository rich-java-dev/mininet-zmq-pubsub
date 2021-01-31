import time
import zmq
import sys

context = zmq.Context()

socket = context.socket(zmq.SUB)

proxy = sys.argv[1] if len(sys.argv) > 1 else "*"
port = sys.argv[2] if len(sys.argv) > 2 else "5556"
topic = sys.argv[3] if len(sys.argv) > 3 else ''

socket.connect(f'tcp://{proxy}:{port}')
socket.setsockopt_string(zmq.SUBSCRIBE, topic)

print(f"Subscriber listening to '{proxy}' w/ topic '{topic}'")

while True:
    msg = socket.recv_string()
    print(msg)
    time.sleep(0.1)
