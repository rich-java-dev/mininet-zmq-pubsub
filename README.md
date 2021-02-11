Environment Dependencies:
- mininet
- python3/pip3 (sudo apt install python3-pip)
- wireshark (sudo pip install wireshark)
- zmq (sudo -H pip3 install (py)zmq)
- pyshark - for monitor/packet analysis (sudo -H pip3 install pyshark )


Sample Network Configuration:

Automatic using main.py:
- please configure main.py to point to the neccessary project directory
- sudo python3 main.py
Run the monitor (not on mininet host):
- sudo python3 monitor.py --interface=any --sample_size=500


Initializing the network:
- sudo mn -c
- sudo mn -x --topo=linear,10

Proxy/Broker: (in_bound, out_bound)
- host1: python3 broker.py --xin=5555 --xout=5556

Publishers: (bind|connect, interface, port, topic_range)
- host2: python3 publisher.py --connect --interface=10.0.0.1 --port=5555 --topic_range 1 49999
- host3: python3 publisher.py --connect --interface=10.0.0.1 --port=5555 --topic_range 50000 100000

Subscribers: (interface, port, topic)
- host4: python3 subscriber.py --interface=10.0.0.1 --port=5556 --topic=12345
- host5: python3 subscriber.py --interface=10.0.0.1 --port=5556 --topic=90210

Monitor: (interface ("s1-eth1",2,3...etc))
- from localhost: sudo python3 monitor.py --interface=any --sample_size=500
