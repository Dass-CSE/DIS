from scapy.all import sniff, IP, TCP
from datetime import datetime

blacklist_ips = ['192.168.1.100', '10.0.0.5']
blacklist_ports = [4444, 5555]

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if src_ip in blacklist_ips or dst_ip in blacklist_ips:
                print(f"[ALERT] [{timestamp}] Suspicious IP detected: {src_ip} -> {dst_ip}")
            if sport in blacklist_ports or dport in blacklist_ports:
                print(f"[ALERT] [{timestamp}] Suspicious port usage: {src_ip}:{sport} -> {dst_ip}:{dport}")

print("Starting IDS... Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=0)
