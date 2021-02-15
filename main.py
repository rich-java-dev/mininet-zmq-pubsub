from mininet.net import Mininet
from mininet.topo import LinearTopo
from mininet.topo import SingleSwitchTopo
import time
from random import randrange
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--broker_mode", default=True)
parser.add_argument("--flood_mode", default=False)
parser.add_argument("--xin", default="5555")  # for use with broker
parser.add_argument("--xout", default="5556")  # for use with broker
parser.add_argument("--topic", default="")
parser.add_argument("--net_size", default=10)
parser.add_argument("--pub_count", default=2)
parser.add_argument("--source_dir", "--src_dir",
                    default="/home/rw/mininet/cs6381-assignment1")
args = parser.parse_args()

host_count = int(args.net_size)
net_topo = LinearTopo(k=host_count)  # feel free to run with other topos

net = Mininet(topo=net_topo)  # create a 10 host net
net.start()

src_dir = args.source_dir
x_intf = "10.0.0.1"  # proxy interface
xin = args.xin  # proxy input (pub connection)
xout = args.xout  # proxy output (sub connection)

# broker.py <proxy_input_port> <proxy_output_port>
prox_str = f'python3 {src_dir}/proxy.py &'
print(prox_str)
net.hosts[0].cmd(prox_str)

# set up publishers
pub_count = int(args.pub_count)
topic_size = 1e5 / pub_count

# pub.py <proxy_interface> <interface_port (proxy subscrib port)> <publisher_range_min> <publisher_range_max>
for i in range(0, pub_count):
    cmd_str = f'python3 {src_dir}/publisher.py --connect --interface={x_intf} --topic_range {int(i*topic_size)} {int((i+1)*topic_size)} &'
    print(cmd_str)
    net.hosts[i].cmd(cmd_str)


# sub.py <proxy_interface> <interface_port (proxy publish port)> <topic>
for i in range(pub_count + 1, host_count):
    topic = randrange(1e4, 1e5)
    cmd_str = f'python3 {src_dir}/subscriber.py --interface={x_intf} --port={xout} --topic={topic} >logs/h{i+1}.log &'
    print(cmd_str)
    net.hosts[i].cmd(cmd_str)

while(True):
    time.sleep(0.001)
