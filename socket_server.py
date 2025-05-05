import socket

if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen()  # List antrian koneksi yang masuk pada server

    while True:
        client, address = server.accept()
        print(f"Conected {address[0]} : {address[1]}")

        inputan_client = client.recv(1024)
        inputan_client = inputan_client.decode("utf-8")
        print(inputan_client)
        client.send(bytes(inputan_client, "utf-8"))

        client.close()
