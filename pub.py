from datetime import datetime
import time
import zmq

context = zmq.Context()

socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5050")

while True:
    socket.send_string(str(datetime.now()))
    time.sleep(1)
