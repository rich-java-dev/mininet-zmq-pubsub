from mininet.net import Mininet
from mininet.topo import LinearTopo
from mininet.topo import SingleSwitchTopo
import time
from random import randrange

net_topo = LinearTopo(k=20)

net = Mininet(topo=net_topo)  # create a 10 host net
net.start()

src_dir = '/home/rw/projects/cs6381-assignment1'

# set up proxy/broker
net.hosts[0].cmd(f'sudo python3 {src_dir}/broker.py &')

# set up publishers
net.hosts[1].cmd(f'sudo python3 {src_dir}/pub.py 10.0.0.1 5555 0 24999 &')
net.hosts[2].cmd(f'sudo python3 {src_dir}/pub.py 10.0.0.1 5555 25000 49999 &')
net.hosts[3].cmd(f'sudo python3 {src_dir}/pub.py 10.0.0.1 5555 50000 74999 &')
net.hosts[3].cmd(f'sudo python3 {src_dir}/pub.py 10.0.0.1 5555 75000 100000 &')

# set up subscribers
for i in range(5, 20):
    topic = randrange(1, 100000)
    net.hosts[i].cmd(f'sudo python3 {src_dir}/sub.py 10.0.0.1 {topic} &')

while(True):
    time.sleep(0.01)
