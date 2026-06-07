import pyshark

# Define the pcap file and the IP address to filter by
pcap_file = 'chall/chall.pcapng'
source_ip = '192.168.216.129'

cap = pyshark.FileCapture(pcap_file, display_filter='icmp')

# Loop through each packet and filter by source IP and ICMP type (echo request)
for packet in cap:
    try:
        if packet.ip.src == source_ip and packet.icmp.type == '8':
            data_hex = packet.icmp.data.replace(':', '')[:32]
            print(data_hex) ## decode hex 2x
            
    except AttributeError:
        # Skip packets that do not have the expected fields
        continue

# Close the capture
cap.close()
