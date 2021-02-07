import pyshark

capture = pyshark.LiveCapture(interface='s1-eth1')

for packet in capture.sniff_continuously(packet_count=50):
    # print(packet)
    ip = packet.ip
    tcp = packet.tcp

    src = ip.src
    dst = ip.dst
    port = tcp.dstport
    flags = tcp.flags
    time_delta = tcp.time_delta
    print(
        f' source: {src} dest: {dst} port: {port} time_lapse(RTT):{time_delta} flags:{flags}')
