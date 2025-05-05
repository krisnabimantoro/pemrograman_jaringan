import socket

ip = "localhost"
port = 9807

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

while True:
    data, address = server.recvfrom(1024)
    data = data.decode("utf-8")
    print(f"Client:{data}")

    data = data.upper()
    data = data.encode("utf-8")
    server.sendto(data, address)
