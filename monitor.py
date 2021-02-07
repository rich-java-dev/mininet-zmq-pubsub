import pyshark
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--interface", default="s1-eth1")
args = parser.parse_args()
intf = args.interface

capture = pyshark.LiveCapture(interface=intf)

for packet in capture.sniff_continuously(packet_count=50):
    # print(packet)
    ip = packet.ip
    tcp = packet.tcp

    src = ip.src
    dst = ip.dst
    port = tcp.dstport

    # filter for zmq transmissions
    if port > 5600:
        continue

    flags = tcp.flags
    time_delta = tcp.time_delta
    print(
        f' source: {src} dest: {dst} port: {port} time_lapse(RTT):{time_delta} flags:{flags}')
