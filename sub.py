import time
import zmq
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--interface", "--proxy","--device", default="*")
parser.add_argument("--port", default="5555")
parser.add_argument("--topic", default="")
parser.add_argument("--bind", action="store_true")
parser.add_argument("--connect", action="store_true")
args = parser.parse_args()

intf = args.interface
port = args.port
topic = args.topic
bind = args.bind
connect = args.connect

context = zmq.Context()
socket = context.socket(zmq.SUB)

conn_str = f'tcp://{intf}:{port}'
print(f'Subscriber pulling from {conn_str}')

if bind:
    print("binding")
    socket.bind(conn_str)

if connect:
    print("connecting")
    socket.connect(conn_str)

socket.setsockopt_string(zmq.SUBSCRIBE, topic)

print(f"Subscriber listening to '{intf}' w/ topic '{topic}'")

while True:
    msg = socket.recv_string()
    print(msg)
    time.sleep(0.1)
