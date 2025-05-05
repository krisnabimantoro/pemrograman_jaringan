import socket
import threading


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break
            print("\n" + message)
        except ConnectionResetError:
            print("Koneksi ke server terputus.")
            break


if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    print("Terhubung ke server. Ketik 'exit' untuk keluar.")

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        try:
            pesan = input()
            if pesan.lower() == "exit":
                break
            client.send(pesan.encode("utf-8"))
        except KeyboardInterrupt:
            break

    client.close()
