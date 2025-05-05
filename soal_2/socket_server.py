# Nama: Krisna Bimantoro
# NIM: 202210370311254


from datetime import datetime
import socket


def perhitunganUmur(tahun_lahir):
    tahun_sekarang = datetime.now().year
    tahun_lahir = int(tahun_lahir)
    umur = tahun_sekarang - tahun_lahir
    return umur


if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()  # List antrian koneksi yang masuk pada server

    while True:
        client, address = server.accept()
        print(f"Terhubung dengan {address[0]} : {address[1]}")

        input_nama = client.recv(1024).decode("utf-8")
        input_nim = client.recv(1024).decode("utf-8")
        input_tahun = client.recv(1024).decode("utf-8")
        umur = perhitunganUmur(input_tahun)

        print(f"Nama: {input_nama}")
        print(f"NIM: {input_nim}")
        print(f"Tahun Lahir: {input_tahun}")
        print(f"Umur: {umur}")

        response = f"Data diterima!\nNama: {input_nama}, NIM: {input_nim}, Tahun Lahir: {input_tahun}, Umur: {umur} tahun"
        
        client.send(response.encode("utf-8"))

        client.close()
