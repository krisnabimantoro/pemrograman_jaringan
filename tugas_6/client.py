import socket
def client_program():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('localhost', 9806))
	print("Tersambung ke server. Ketik 'exit' untuk keluar.")
	client.close()

if __name__ == '__main__':
	client_program()
