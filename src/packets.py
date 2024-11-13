from scapy.all import *

packet = IP(src="46.17.46.213", dst="172.17.0.2") / TCP(dport=80, flags="S")
packet2 = IP(src="46.17.46.214", dst="172.17.0.2") / TCP(dport=80, flags="S")
packet3 = IP(src="46.17.46.215", dst="172.17.0.2") / TCP(dport=80, flags="S")

send(packet, iface="eth0")
send(packet2, iface="eth0")
send(packet3, iface="eth0")
