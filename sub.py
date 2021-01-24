import time
import zmq
import sys

context = zmq.Context()

socket = context.socket(zmq.SUB)

pub_server = sys.argv[1] if len(sys.argv) > 1 else "localhost"
socket.connect("tcp://" + pub_server + ":5050")

socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    msg = socket.recv_string()
    print(msg)
    time.sleep(1)
