# Nama: Krisna Bimantoro
# NIM: 202210370311254

import socket
if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    input_p = input("Masukan Panjang : ")
    server.send(bytes(input_p, "utf-8"))
    input_l = input("Masukan Lebar : ")
    server.send(bytes(input_l, "utf-8"))
    
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")
    print("Server :", buffer)
