
import socket
host = "localhost"
port = 9806

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((host,port))

input_nama = input("Masukan Nama : ")
server.send(bytes(input_nama, "utf-8"))

buffer = server.recv(1024)
buffer