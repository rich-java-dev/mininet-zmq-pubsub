from mininet.net import Mininet
from mininet.topo import LinearTopo
import time

net_topo = LinearTopo(k=20)

net = Mininet(topo=net_topo)  # create a 10 host net
net.start()

src_dir ='/home/rw/projects/cs6381-assignment1'

net.hosts[0].cmd(f'sudo python3 {src_dir}/broker.py &')

net.hosts[1].cmd(f'sudo python3 {src_dir}/pub.py &')
net.hosts[2].cmd(f'sudo python3 {src_dir}/sub.py 10.0.0.1 &')

while(True):
    time.sleep(0.1)
