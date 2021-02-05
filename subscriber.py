import sys
import time
import argparse
from zutils import subscriber

parser = argparse.ArgumentParser()
parser.add_argument("--interface", "--proxy",
                    "--device", nargs="+", default="*")
parser.add_argument("--port", default="5555")
parser.add_argument("--topic", default="")
parser.add_argument("--net_size", default=0)
args = parser.parse_args()

intf = args.interface
port = args.port
topic = args.topic
net_size=args.net_size

notify = subscriber(intf, port, topic, net_size)

while True:
    msg = notify()
    print(msg)
    time.sleep(0.1)
