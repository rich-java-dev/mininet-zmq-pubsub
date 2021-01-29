Sample Network Configuration:

Proxy/Broker: (in_bound, out_bound)
- host1: python3 broker.py 5555 5556


Publishers: (interface, out_bound (proxy in_bound), min_range, max_range)
- host2: python3 pub.py 10.0.0.1 5555 1 49999
- host3: python3 pub.py 10.0.0.1 5555 50000 100000


Subscribers: (interface, topic, in_bound (proxy out_bound))
- host4: python3 sub.py 10.0.0.1 90210 5556
- host5: python3 sub.py 10.0.0.1 12345 5556
