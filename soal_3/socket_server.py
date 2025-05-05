import socket
import threading

clients = []


def handle_client(client, addr):
    print(f"[TERHUBUNG] {addr} telah terhubung.")

    while True:

        message = client.recv(1024).decode("utf-8")
        if not message:
            break  # Keluar jika client menutup koneksi

        print(f"[{addr}] {message}")

        for c in clients:
            if c != client:
                c.send(f"{addr}: {message}".encode("utf-8"))

    print(f"[PUTUS] {addr} telah keluar.")
    clients.remove(client)
    client.close()


if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(2)
    print(f"Server berjalan di {ip}:{port}, menunggu 2 client...")

    while len(clients) < 2:
        client, addr = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()
