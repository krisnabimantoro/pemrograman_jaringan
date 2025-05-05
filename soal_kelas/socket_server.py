# Nama: Krisna Bimantoro
# NIM: 202210370311254


from datetime import datetime
import socket


def Luas(p, l):
    luas = p*l
    return luas


if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()  # List antrian koneksi yang masuk pada server

    while True:
        client, address = server.accept()
        print(f"Terhubung dengan {address[0]} : {address[1]}")

        input_p = int(client.recv(1024).decode("utf-8"))
        input_l = int(client.recv(1024).decode("utf-8"))
        luas = Luas(input_p, input_l)

        print(f"Panjang: {input_p}")
        print(f"Lebar: {input_l}")
        print(f"Lebar: {luas}")

        response = f"Data diterima!\Panjang: {input_p}, Lebar: {input_l}, Luas: {luas}"
        client.send(response.encode("utf-8"))

        client.close()
