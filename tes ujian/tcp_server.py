import socket

host = "localhost"
port = 9806

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(host,port)
server.listen()

while True:
    client,address = server.accept()
    
    inputan = client.recv(1024).decode("utf-8")
    print(f"Client: {inputan}")
    
    response = "tes"
    client.send(response.encode("utf-8"))
    client.close()    