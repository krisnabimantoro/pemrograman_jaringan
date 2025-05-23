import socket
import logging

logging.basicConfig(
    filename="honeypot.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

if __name__ == "__main__":
    ip = "localhost"
    port = 9806
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()  # List antrian koneksi yang masuk pada server
    while True:
        conn, address = server.accept()
        logging.info(f"Koneksi dari {ip}:{port}")
        print(f"Conected {address[0]} : {address[1]}")
        info_dummy = "SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n"
        conn.sendall(info_dummy.encode())
        conn.close()
