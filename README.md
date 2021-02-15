## Environment Dependencies:
- mininet
- python3/pip3 (sudo apt install python3-pip)
- wireshark (sudo pip install wireshark)
- zmq (sudo -H pip3 install (py)zmq)
- pyshark - for monitor/packet analysis (sudo -H pip3 install pyshark )


## App Structure

- publisher
usage: publisher.py [-h] [--interface INTERFACE [INTERFACE ...]] [--port PORT]
                    [--topic_range TOPIC_RANGE [TOPIC_RANGE ...]] [--bind] [--connect]

optional arguments:
  -h, --help            show this help message and exit
  --interface INTERFACE [INTERFACE ...], --proxy INTERFACE [INTERFACE ...], --device INTERFACE [INTERFACE ...]
  --port PORT
  --topic_range TOPIC_RANGE [TOPIC_RANGE ...]
  --bind
  --connect



- subscriber
usage: subscriber.py [-h] [--interface INTERFACE [INTERFACE ...]] [--port PORT] [--topic TOPIC] [--net_size NET_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  --interface INTERFACE [INTERFACE ...], --proxy INTERFACE [INTERFACE ...], --device INTERFACE [INTERFACE ...]
  --port PORT
  --topic TOPIC
  --net_size NET_SIZE



- proxy
usage: proxy.py --xin=5555 --xout=5556 [-h] [--xin XIN] [--xout XOUT]

optional arguments:
  -h, --help            show this help message and exit
  --xin XIN, --in_bound XIN
  --xout XOUT, --out_bound XOUT




- monitor (pyshark api for monitoring TCP packets (TTDs)) - must be ran as root/sudo
usage: monitor.py [-h] [--interface INTERFACE] [--net_size NET_SIZE]
                  [--sample_size SAMPLE_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  --interface INTERFACE
  --net_size NET_SIZE
  --sample_size SAMPLE_SIZE, --samples SAMPLE_SIZE




- main (driver for configuring network)


- zutils (api wrapper)
We went with implementing callbacks vs. a more strict/formal OOP/class structure. The result is that both publishers and subscribers return a lambda which behaves as a 'thunk'.



## Sample Network Configuration:

Automatic using main.py:
- please configure main.py to point to the neccessary project directory (via the )
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
