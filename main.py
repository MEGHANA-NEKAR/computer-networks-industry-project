# A port scanner is an application designed to probe a server or host for open ports.
# Such an application may be used by administrators to verify security policies of their networks 
# and by attackers to identify network services running on a host and exploit vulnerabilities

from ast import arg
from tkinter import font
import pyfiglet
import sys
import socket
from datetime import datetime
import scapy.all as scapy
import subprocess


ascii_banner = pyfiglet.figlet_format("PORT SCANNING",font="digital")
print(ascii_banner)

# Defining a target
if len(sys.argv) == 2:
	
	# translate hostname to IPv4
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of Argument")

# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)


	
# will scan ports between 1 to 65,535
for port in range(1,65535):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    # returns an error indicator
    result = s.connect_ex((target,port))
    if result ==0:
        print("Port {} is open".format(port))
    s.close()


# Scanning of the whole network to which we are connected and try to find out what are all the clients connected
# to our network. We can identify each client using their IP and MAC address.
# We can use ARP ping to find out the alive systems in our network.


# The network scanner will send the ARP request indicating who has some specific IP address, let’s say “192.168.1.1”, 
# the owner of that IP address ( the target ) will automatically respond saying that he is “192.168.1.1”, with that response,
# the MAC address will also be included in the packet, this allows us to successfully retrieve all network users’ IP and MAC addresses simultaneously
# when we send a broadcast packet ( sending a packet to all the devices in the network ).


# Create an ARP packet using ARP() method.
# Set the network range using a variable.
# Create an Ethernet packet using Ether() method.
# Set the destination to broadcast using variable hwdst.
# Combine ARP request packet and Ethernet frame using ‘/’.
# Send this to your network and capture the response from different devices.#scapy.srp()
# Print the IP and MAC address from the response packets.
ascii_banner = pyfiglet.figlet_format("NETWORK SCANNING",font="digital")
print(ascii_banner)
request = scapy.ARP()
request.pdst = sys.argv[1] #127.0.0.1
broadcast = scapy.Ether()
	
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
	
request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0]
for element in clients:
	print(element[1].psrc + "	 " + element[1].hwsrc)

# Here x = Network range. For example x = 192.168.0.1/24, 172.16.5.1/16 etc

# pdst is where the ARP packet should go (target),
# psrc is the IP to update in the target’s arp table,
# hwsrc is the sender’s hardware address.
# hwdst is a target hardware address    

# It is also known by using ‘ping command’.
# An ICMP packet is sent to a host using the IP address and if the ICMP echo is received,
# that means that the host is online and is receiving the signals. 
# For this, it necessary to get all the IP addresses for which you wish to test that the host is connected or not. 
# This method works on the assumption that network devices have ICMP enabled.
ascii_banner = pyfiglet.figlet_format("ICMP SCANNING",font="digital")
print(ascii_banner)
for ping in range(1,10):
    address = "127.0.0." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print( "ping to", address, "OK")
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
		
