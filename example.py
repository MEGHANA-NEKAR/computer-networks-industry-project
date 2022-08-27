#! /usr/bin/env python
from scapy.all import *

ip_layer = IP(dst="172.16.27.135")
icmp_layer = ICMP(seq=9999)
packet = ip_layer / icmp_layer
send(packet)