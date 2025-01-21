from scapy.all import sniff, wrpcap
import os

CAPTURE_FILE = "data/raw/network_traffic.pcap"

def packet_handler(packet):
    print(f"Captured Packet: {packet.summary()}")

def start_capture():
    if not os.path.exists("data/raw"):
        os.makedirs("data/raw")
    print("Starting packet capture...")
    sniff(prn=packet_handler, count=100)  # Capture 100 packets
    wrpcap(CAPTURE_FILE, sniff(count=100))
    print(f"Traffic saved to {CAPTURE_FILE}")
