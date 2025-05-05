import tkinter as tk
from tkinter import ttk

import socket

ip = "localhost"
port = 9807
address = (ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

window = tk.Tk()

window.configure(bg='white')
window.geometry("500x800")
window.title("Aplikasi Saya")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, fill='x', expand=True)

nama_depan_label = ttk.Label(input_frame, text="Pesan: ")
nama_depan_label.pack(padx=10, fill='x', expand=True)

PESAN = tk.StringVar()
nama_depan_input = ttk.Entry(input_frame, textvariable=PESAN)
nama_depan_input.pack(padx=10, fill='x', expand=True)


def send_message():
    message = PESAN.get().encode("utf-8")
    client.sendto(message, address)
    response, _ = client.recvfrom(1024)
    response = response.decode("utf-8")
    print(f"Server: {response}")

window.bind("<Return>", lambda x: send_message())

login_button = ttk.Button(input_frame, text="SEND MESSAGE", command=send_message)



login_button.pack(fill='x', expand=True, pady=10)

window.mainloop()
