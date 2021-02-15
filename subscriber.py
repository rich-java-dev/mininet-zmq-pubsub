import sys
import time
import argparse
from zutils import subscriber
import datetime
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--interface", "--proxy",
                    "--device", nargs="+", default="*")
parser.add_argument("--port", default="5556")
parser.add_argument("--topic", default="")
parser.add_argument("--net_size", default=0)
parser.add_argument("--sample_size", "--samples", default=50)
parser.add_argument("--label", default="")

args = parser.parse_args()

intf = args.interface
port = args.port
topic = args.topic
net_size = int(args.net_size)
sample_size = int(args.sample_size)
label = args.label

notify = subscriber(intf, port, topic, net_size)

delta_time_set = []
while len(delta_time_set) < sample_size:
    msg = notify()
    ts = time.time()
    msg_time = float(msg.split(" ")[-1])
    delta = ts - msg_time

    delta_time_set.append(delta)
    print(msg)

# plot the time deltas
fig, axs = plt.subplots(1)
axs.plot(range(len(delta_time_set)), delta_time_set)
axs.set_title(f"RTTs (Round Trip Time) '{label}' - topic '{topic}'")
plt.show()
