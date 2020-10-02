from socket import *

HOSTNAME    = 'localhost'
PORT        = 1337

sock = socket(AF_INET, SOCK_DGRAM)

server_address = (HOSTNAME, PORT)

print('[+] Starting up on {} port {}'.format(*server_address))

sock.bind(server_address)

while 1:
    print('[+] Waiting for a connection')
    data, client_address = sock.recvfrom(1024)
    print(f'[+] Received: {data.decode()}')
