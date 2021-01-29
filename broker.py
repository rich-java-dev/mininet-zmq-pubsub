import zmq
import sys

context = zmq.Context()

in_bound = sys.argv[1] if len(sys.argv) > 1 else "5555"
out_bound = sys.argv[2] if len(sys.argv) > 2 else "5556"


# connects our Publishers to the Broker
front_end = context.socket(zmq.XSUB)
front_end.bind(f"tcp://*:{in_bound}")

# connects our  Subscribers to the Broker
back_end = context.socket(zmq.XPUB)
back_end.setsockopt(zmq.XPUB_VERBOSE, 1)
back_end.bind(f"tcp://*:{out_bound}")

zmq.proxy(front_end, back_end)
