import sys
import time
import argparse
from netutils import subscriber

parser = argparse.ArgumentParser()
parser.add_argument("--interface", "--proxy",
                    "--device", nargs="+", default="*")
parser.add_argument("--port", default="5555")
parser.add_argument("--topic", default="")
parser.add_argument("--bind", action="store_true")
parser.add_argument("--connect", action="store_true")
args = parser.parse_args()

intf = args.interface
port = args.port
bind = args.bind
connect = args.connect
topic = args.topic

sub = subscriber(intf, port, bind, connect, topic)

while True:
    msg = sub()
    print(msg)
    time.sleep(0.1)
