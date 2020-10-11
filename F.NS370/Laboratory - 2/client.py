from socket import *

HOSTNAME    = 'localhost'
PORT        = 1337

sock = socket(AF_INET, SOCK_DGRAM)

server_address = (HOSTNAME, PORT)

print('[+] Connecting to {} port {}'.format(*server_address))

sock.connect(server_address)

try:
    message = b'This is our message. And its too long so dont worry'
    print('[+] Sending {!r}'.format(message))
    sock.sendall(message)

finally:
    print(f'[+] Sending data successfully')
    print(f'[+] Closing connection')
    sock.close()