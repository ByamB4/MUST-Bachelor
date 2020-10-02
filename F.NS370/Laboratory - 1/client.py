from socket import *

HOSTNAME    = 'localhost'
PORT        = 1337

sock = socket(AF_INET, SOCK_STREAM)

server_address = (HOSTNAME, PORT)

print('[+] Connecting to {} port {}'.format(*server_address))

sock.connect(server_address)

try:
    message = b'This is our message. And its too fucking long okay so dont worry'
    print('[+] Sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))
finally:
    print('closing socket')
