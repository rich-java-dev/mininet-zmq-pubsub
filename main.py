from mininet.net import Mininet
from mininet.topo import LinearTopo
import time

net_topo = LinearTopo(k=10)

net = Mininet(topo=net_topo)  # create a 10 host net
net.start()

net.hosts[0].cmd('sudo python3 /home/rw/projects/cs6381-assignment1/pub.py &')
net.hosts[1].cmd('sudo python3 /home/rw/projects/cs6381-assignment1/sub.py 10.0.0.1 &')

while(True):
    time.sleep(1)
