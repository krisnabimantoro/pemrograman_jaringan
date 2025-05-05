import socket
import ssl
HOST = 'localhost'
PORT = 4444


def get_message():
    context = ssl._create_unverified_context(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('new.pem')
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_soc = context.wrap_socket(soc, server_hostname=HOST)
    c_soc.connect((HOST, PORT))
    print("Connection Success")
   
    msg = c_soc.recv(1024)
    print(msg.decode("utf-8"))

   
    input_nama = input("Masukan Nama : ")
    c_soc.send(bytes(input_nama, "utf-8"))
   
    input_nim = input("Masukan NIM : ")
    c_soc.send(bytes(input_nim, "utf-8"))
   
    input_tahun = input("Masukan Tahun Lahir : ")
    c_soc.send(bytes(input_tahun, "utf-8"))

    output = c_soc.recv(1024)
    print(output.decode("utf-8"))

    c_soc.close()


if __name__ == "__main__":
    get_message()
