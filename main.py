import logging
from scapy.all import *
from colorama import init, Fore, Style

# Initialize colorama for colored logs in the terminal
init(autoreset=True)

# Set up logging to format the output (with color support)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def log_packet_details(ip_src, ip_dst, protocol, layer_details):
    """
    Logs packet details with color formatting for better readability.
    """
    logging.info(f"{Fore.GREEN}--- Packet Captured ---{Style.RESET_ALL}")
    logging.info(f"{Fore.CYAN}Source IP: {ip_src}{Style.RESET_ALL}")
    logging.info(f"{Fore.CYAN}Destination IP: {ip_dst}{Style.RESET_ALL}")
    logging.info(f"{Fore.YELLOW}Protocol: {protocol}{Style.RESET_ALL}")
    
    # Log the details based on the protocol
    if layer_details.get('protocol') == 'TCP':
        logging.info(f"{Fore.BLUE}TCP Source Port: {layer_details.get('sport')}{Style.RESET_ALL}")
        logging.info(f"{Fore.BLUE}TCP Destination Port: {layer_details.get('dport')}{Style.RESET_ALL}")
    elif layer_details.get('protocol') == 'UDP':
        logging.info(f"{Fore.BLUE}UDP Source Port: {layer_details.get('sport')}{Style.RESET_ALL}")
        logging.info(f"{Fore.BLUE}UDP Destination Port: {layer_details.get('dport')}{Style.RESET_ALL}")
    elif layer_details.get('protocol') == 'ARP':
        logging.info(f"{Fore.MAGENTA}ARP Request: {layer_details.get('psrc')} -> {layer_details.get('pdst')}{Style.RESET_ALL}")
    else:
        logging.info(f"{Fore.RED}Non-TCP/UDP packet detected!{Style.RESET_ALL}")
    
    logging.info(f"{Fore.GREEN}---------------------------{Style.RESET_ALL}")

def packet_callback(packet):
    """
    Called for every packet captured. Extracts and logs details based on the packet's content.
    """
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        layer_details = {}

        # Determine protocol layer details
        if packet.haslayer(TCP):
            layer_details = {'protocol': 'TCP', 'sport': packet[TCP].sport, 'dport': packet[TCP].dport}
        elif packet.haslayer(UDP):
            layer_details = {'protocol': 'UDP', 'sport': packet[UDP].sport, 'dport': packet[UDP].dport}
        elif packet.haslayer(ARP):
            layer_details = {'protocol': 'ARP', 'psrc': packet[ARP].psrc, 'pdst': packet[ARP].pdst}
        else:
            layer_details = {'protocol': 'Unknown'}

        # Log the packet details
        log_packet_details(ip_src, ip_dst, protocol, layer_details)
    else:
        logging.info(f"{Fore.RED}Non-IP Packet captured!{Style.RESET_ALL}")

def start_packet_capture():
    """
    Starts the packet capture and logs the starting message.
    """
    logging.info(f"{Fore.GREEN}Starting Cybersecurity Monitoring System...{Style.RESET_ALL}")
    logging.info(f"{Fore.YELLOW}Starting packet capture... Press Ctrl+C to stop.{Style.RESET_ALL}")
    sniff(prn=packet_callback, store=0, count=0)  # Infinite sniffing until manually stopped

if __name__ == "__main__":
    start_packet_capture()
