import zmq
from random import randrange
import time
import sys

context = zmq.Context()
socket = context.socket(zmq.PUB)

proxy = sys.argv[1] if len(sys.argv) > 1 else "*"
port = sys.argv[2] if len(sys.argv) > 2 else "5555"
lower_bound = sys.argv[3] if len(sys.argv) > 3 else 0
upper_bound = sys.argv[4] if len(sys.argv) > 4 else 100000

conn_str = f'tcp://{proxy}:{port}'
print(f'Publisher pushing to {conn_str}')

socket.connect(conn_str)


while True:
    zipcode = randrange(int(lower_bound), int(upper_bound))
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)

    socket.send_string("%i %i %i" % (zipcode, temperature, relhumidity))
