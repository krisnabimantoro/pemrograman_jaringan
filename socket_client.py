import socket
if __name__ == "__main__":
    ip = "localhost"
    port = 9806

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip, port))

    input_angka = input("Masukan Angka : ")
    server.send(bytes(input_angka, "utf-8"))
    buffer = server.recv(1024)
    buffer = buffer.decode("utf-8")
    print("Server :", buffer)
