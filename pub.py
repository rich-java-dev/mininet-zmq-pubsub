import zmq
from random import randrange
import time
import sys

context = zmq.Context()
socket = context.socket(zmq.PUB)

port = "5555"
proxy = sys.argv[1] if len(sys.argv) > 1 else "*"

conn_str = f'tcp://{proxy}:{port}'
print(f"Publisher pushing to {conn_str}")

socket.bind(conn_str)


while True:
    zipcode = randrange(1, 100000)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))
    time.sleep(0.1)
