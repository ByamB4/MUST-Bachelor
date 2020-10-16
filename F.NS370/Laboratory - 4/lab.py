from scapy.all import ARP, Ether, srp

NETWORK = "10.4.201.0/24"
arp = ARP(pdst=NETWORK)
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = broadcast / arp
print(f'[+] Builded packet: {packet}')
result = srp(packet, timeout=3, verbose=0)[0]

clients = []

for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("IP" + " " * 18 + "MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
