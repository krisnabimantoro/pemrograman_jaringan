import socket

host = "localhost"
port = 9806

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((host,port))

while True:
    data,address  = server.recvfrom(1024)
    data = data.decode("utf-8") 
    
    data = data.upper()
    data = data.encode("utf-8")
    server.sendto(data,address)