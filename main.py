from mininet.net import Mininet
from mininet.topo import LinearTopo
from mininet.node import OVSController

net_topo = LinearTopo(k=10)

net = Mininet(topo=net_topo, controller=OVSController)  # create a 10 host net
net.start()

net.ping()
net.stop()
