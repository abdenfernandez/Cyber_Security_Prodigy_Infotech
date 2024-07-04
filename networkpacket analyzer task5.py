pip install scapy


from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        print(f"\nPacket captured:")
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        
        # Check for TCP protocol
        if protocol == 6:
            print("Protocol: TCP")
            if TCP in packet:
                payload = packet[TCP].payload
                print(f"Payload: {payload}")
                
        # Check for UDP protocol
        elif protocol == 17:
            print("Protocol: UDP")
            if UDP in packet:
                payload = packet[UDP].payload
                print(f"Payload: {payload}")
        
# Start sniffing
print("Starting packet sniffer...")
sniff(prn=packet_callback, store=0)
