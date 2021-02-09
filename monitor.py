import pyshark
import argparse
from multiprocessing import Pool
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--interface", default="s1-eth1")
parser.add_argument("--net_size", default=1)
parser.add_argument("--sample_size", "--samples", default=50)

args = parser.parse_args()
intf = args.interface
sample_size = args.sample_size
net_size = int(args.net_size)


def capture_and_plot(intf):
    print(f"begining live capture on {intf}")

    capture = pyshark.LiveCapture(interface=intf)
    packet_map = {}
    for packet in capture.sniff_continuously(packet_count=sample_size):
        # print(packet)

        if "ip" not in packet or "tcp" not in packet:
            continue

        ip = packet.ip
        tcp = packet.tcp

        port = tcp.dstport

        src = ip.src
        dst = ip.dst

        flags = tcp.flags
        time_delta = tcp.time_delta

        key = f'{src}/{dst}:{port}'
        if key in packet_map:
            data_points = packet_map[key]
            data_points.append(float(time_delta))
        else:
            data_points = [float(time_delta), ]
            packet_map[key] = data_points

        print(
            f' source: {src} dest: {dst} port: {port} time_lapse(RTT):{time_delta} flags:{flags}')

    fig, axs = plt.subplots(len(packet_map))
    fig.suptitle('RTTs (round trip time) of Packets')

    i = 0
    for k, v in packet_map.items():
        axs[i].plot(range(len(v)), v)
        axs[i].set_title(f'(src/dest:port) - {k}')
        i = i+1
    plt.show()


# p = Pool(net_size)
# with p:
#     p.map(capture_and_plot, range(net_size))
if net_size == 1:
    capture_and_plot(intf)
else:
    for i in range(net_size):
        intf = f"s1-eth{i+1}"
        capture_and_plot(intf)

plt.show()
