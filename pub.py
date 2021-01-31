import zmq
from random import randrange
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--interface", "--proxy", "--device", nargs="+", default="*")
parser.add_argument("--port", default="5555")
parser.add_argument("--topic_range", nargs="+")
parser.add_argument("--bind", action="store_true", default=False)
parser.add_argument("--connect", action="store_true", default=False)
args = parser.parse_args()

intf = args.interface
port = args.port
lower_bound = args.topic_range[0]
upper_bound = args.topic_range[1]

print(lower_bound)
print(upper_bound)

bind = args.bind
connect = args.connect

context = zmq.Context()
socket = context.socket(zmq.PUB)

conn_str = f'tcp://{intf}:{port}'
print(
    f'Publisher pushing to {conn_str} w/ topic range:[{lower_bound},{upper_bound}]')

if bind:
    print("binding")
    socket.bind(conn_str)

if connect:
    for interface in intf:
        conn_str = f'tcp://{interface}:{port}'
        print(f"connecting: {conn_str}")
        socket.connect(conn_str)

while True:
    zipcode = randrange(int(lower_bound), int(upper_bound))
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)
    msg = "%i %i %i" % (zipcode, temperature, relhumidity)
    socket.send_string(msg)
