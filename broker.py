import zmq
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--xin", "--in_bound", default="5555")
parser.add_argument("--xout", "--out_bound", default="5556")
args = parser.parse_args()

in_bound = args.xin
out_bound = args.xout

context = zmq.Context()

# connects our Publishers to the Broker
front_end = context.socket(zmq.XSUB)
front_end.bind(f"tcp://*:{in_bound}")

# connects our  Subscribers to the Broker
back_end = context.socket(zmq.XPUB)
back_end.setsockopt(zmq.XPUB_VERBOSE, 1)
back_end.bind(f"tcp://*:{out_bound}")

print(f"Broker/Proxy started with in_bound={in_bound}, out_bound={out_bound}")

zmq.proxy(front_end, back_end)
