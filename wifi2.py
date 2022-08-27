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


import scapy.all as scapy

request = scapy.ARP()
print("ARP Request Packet Summary: ",request.summary())
print("-" * 50)
print("ARP Request Packet .show(): ",request.show())
print("-" * 50)
print("LS Command ",scapy.ls(scapy.ARP()))	
print("-" * 50)
request.pdst = '192.168.0.1/24'
broadcast = scapy.Ether() #creating ethernet packet
	
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
	
request_broadcast = broadcast / request 
#combining 2 layers, network layer (request IP packet) and link layer (broadcast Ethernet frame)

clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0]
for element in clients:
	print(element[1].psrc + "	 " + element[1].hwsrc)

# Here x = Network range. For example x = 192.168.0.1/24, 172.16.5.1/16 etc

# pdst is where the ARP packet should go (target),
# psrc is the IP to update in the target’s arp table,
# hwsrc is the sender’s hardware address.
# hwdst is a target hardware address    
