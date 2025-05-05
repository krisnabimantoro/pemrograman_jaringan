# Nama: Krisna Bimantoro
# NIM: 202210370311254

import socket
if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    input_nama = input("Masukan Nama : ")
    server.send(bytes(input_nama, "utf-8"))
    input_nim = input("Masukan NIM : ")
    server.send(bytes(input_nim, "utf-8"))
    input_tahun = input("Masukan Tahun Lahir : ")
    server.send(bytes(input_tahun, "utf-8"))
    
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")
    print("Server :", buffer)
