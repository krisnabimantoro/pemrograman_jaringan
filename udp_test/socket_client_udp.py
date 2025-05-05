import socket

ip = "localhost"    
port = 9807
address = (ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("Input Teks ")
    data = data.encode("utf-8")
    
    client.sendto(data, address)    
    
    data, address = client.recvfrom(1024)
    data = data.decode("utf-8")
    print(f"Server: {data}")