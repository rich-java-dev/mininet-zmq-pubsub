import zmq

context = zmq.Context()

# connects our Publishers to the Broker
front_end = context.socket(zmq.XSUB)
front_end.bind("tcp://*:5555")

# connects our  Subscribers to the Broker
back_end = context.socket(zmq.XPUB)
back_end.setsockopt(zmq.XPUB_VERBOSE, 1)
back_end.bind("tcp://*:5556")

zmq.proxy(front_end, back_end)