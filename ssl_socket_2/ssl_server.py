import socket
import ssl
from datetime import datetime

HOST = 'localhost'
PORT = 4444


def perhitunganUmur(tahun_lahir):
    tahun_sekarang = datetime.now().year
    tahun_lahir = int(tahun_lahir)
    umur = tahun_sekarang - tahun_lahir
    return umur


def get_server_conection():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('new.pem', 'private.key')
    soc = socket.socket()
    soc.bind((HOST, PORT))
    print(f"Server is running at '{HOST}' with '{PORT}' .")
    print("Server is ready to request ")

    soc.listen(3)
    s_soc = context.wrap_socket(soc, server_side=True)
    conn, add = s_soc.accept()

    print(f"Server is connect to {add}")
    conn.send(bytes(f"welcome to server ('{HOST}','{PORT}') ...", 'utf-8'))

    input_nama = conn.recv(1024).decode("utf-8")
    input_nim = conn.recv(1024).decode("utf-8")
    input_tahun = conn.recv(1024).decode("utf-8")
    umur = perhitunganUmur(input_tahun)

    print(f"Nama: {input_nama}")
    print(f"NIM: {input_nim}")
    print(f"Tahun Lahir: {input_tahun}")
    print(f"Umur: {umur}")

    response = f"Data diterima!\nNama: {input_nama}, NIM: {input_nim}, Tahun Lahir: {input_tahun}, Umur: {umur} tahun"
    
    conn.send(response.encode("utf-8"))
    s_soc.close()


if __name__ == "__main__":
    get_server_conection()
