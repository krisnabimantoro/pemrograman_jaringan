import socket
import ssl
HOST = 'localhost'
PORT = 4444


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
    print(f"Client: {input_nama}")
    
    input_nim = conn.recv(1024).decode("utf-8")
    print(f"Client: {input_nim}")
    
    input_tahun = conn.recv(1024).decode("utf-8")
    print(f"Client: {input_tahun}")
    
    conn.send(bytes(f"Halo {input_nama} dengan NIM {input_nim} dan Tahun Kelahiran {input_tahun}", 'utf-8'))
    s_soc.close()


if __name__ == "__main__":
    get_server_conection()
