import zmq

context = zmq.Context()

def proxy(in_bound, out_bound):

    # many SUB handling
    front_end = context.socket(zmq.XSUB)
    front_end.bind(f"tcp://*:{in_bound}")

    # many PUB handling
    back_end = context.socket(zmq.XPUB)
    back_end.setsockopt(zmq.XPUB_VERBOSE, 1)
    back_end.bind(f"tcp://*:{out_bound}")

    print(f"Proxy started w/ in_bound={in_bound}, out_bound={out_bound}")

    zmq.proxy(front_end, back_end)


def publisher(interface, port=5555, bind=False, connect=False, topic_min=0, topic_max=100000):
    conn_str = f'tcp://{interface}:{port}'
    socket = context.socket(zmq.PUB)

    print(
        f'Publishing to {conn_str} w/ topic range:[{topic_min},{topic_max}]')

    if bind:
        print("binding")
        socket.bind(conn_str)

    if connect:
        for intf in interface:
            conn_str = f'tcp://{intf}:{port}'
            print(f"connecting: {conn_str}")
            socket.connect(conn_str)

    return lambda msg: socket.send_string(msg)
    

def subscriber(interface, port=5556, bind=False, connect=False, topic=''):
    conn_str = f'tcp://{interface}:{port}'

    socket = context.socket(zmq.SUB)
    if bind:
        print("binding")
        socket.bind(conn_str)

    if connect:
        print(type(interface))
        for intf in interface:
            conn_str = f'tcp://{intf}:{port}'
            print(f"connecting: {conn_str}")
            socket.connect(conn_str)

    socket.setsockopt_string(zmq.SUBSCRIBE, topic)

    print(f"Subscribing to '{conn_str}' w/ topic '{topic}'")

    return lambda: socket.recv_string()

