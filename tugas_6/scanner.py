import socket
def scan_ports(host, ports):
	print(f"Scanning host: {host}")
	for port in ports:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = sock.connect_ex((host, port))
		if result == 0:
			print(f"Port {port} is OPEN")
		else:
			print(f"Port {port} is CLOSED")
		sock.close()

# Contoh penggunaan
target_ip = "krisnabmntr.my.id"  
ports_to_scan = [21, 22, 23, 80, 443, 9806]
scan_ports(target_ip, ports_to_scan)
