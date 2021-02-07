from mininet.net import Mininet
from mininet.topo import LinearTopo
from mininet.topo import SingleSwitchTopo
import time
from random import randrange

host_count = 5
net_topo = LinearTopo(k=host_count)

net = Mininet(topo=net_topo)  # create a 10 host net
net.start()

src_dir = '/home/rw/mininet/cs6381-assignment1'
x_intf = "10.0.0.1"  # proxy interface
xin = "5555"  # proxy input (pub connection)
xout = "5556"  # proxy output (sub connection)

# broker.py <proxy_input_port> <proxy_output_port>
prox_str = f'python3 {src_dir}/proxy.py &'
print(prox_str)
net.hosts[0].cmd(prox_str)

# set up publishers
pub_count = 2

# pub.py <proxy_interface> <interface_port (proxy subscrib port)> <publisher_range_min> <publisher_range_max>
for i in range(0, pub_count):
    cmd_str = f'python3 {src_dir}/publisher.py --connect --interface={x_intf} &'
    print(cmd_str)
    net.hosts[i].cmd(cmd_str)


# sub.py <proxy_interface> <interface_port (proxy publish port)> <topic>
for i in range(pub_count + 1, host_count):
    topic = randrange(1, 100000)
    cmd_str = f'python3 {src_dir}/subscriber.py --interface={x_intf} --port={xout} &'
    print(cmd_str)
    net.hosts[i].cmd(cmd_str)

while(True):
    time.sleep(0.01)
