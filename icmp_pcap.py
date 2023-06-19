#!/usr/bin/python3
from scapy.all import *

def process_packet(packet):
   	 if packet.haslayer(ICMP):
       		 print("ICMP Packet:")
        	 print(packet[IP].src)  # Display detailed information about the packet

# Path to the Packet Tracer file
file_path = "/home/shuhari/resource/demo.pcap"

# Read the Packet Tracer file and process each packet
packets = rdpcap(file_path)
for packet in packets:
    process_packet(packet)

