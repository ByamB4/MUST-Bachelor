from socket import *

HOSTNAME    = 'localhost'
PORT        = 1337

sock = socket(AF_INET, SOCK_STREAM)

server_address = (HOSTNAME, PORT)

print('[+] Starting up on {} port {}'.format(*server_address))

sock.bind(server_address)

sock.listen(1)

while 1:
    print('[+] Waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print(f'[+] Connection from: {client_address}')
        while 1:
            data = connection.recv(16)
            print('[+] Received {}'.format(data))
            if data:
                print('[+] Sending data back to the client')
                connection.sendall(data)
            else:
                print(f'[-] No data from: {client_address}')
                break
    except Exception as e:
        print(e)