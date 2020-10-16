import socket

ADDR, PORT = "127.0.0.1", 1337
data = "Test2\n"

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcp_client.connect((ADDR, PORT))
    tcp_client.sendall(data.encode())

    received = tcp_client.recv(1024)
finally:
    tcp_client.close()

print(f"Bytes Sent:     {data}")
print(f"Bytes Received: {received.decode()}")
