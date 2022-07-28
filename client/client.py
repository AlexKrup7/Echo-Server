import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 2000))

msg = 'hi, i`m groot'
client_socket.send(msg.encode())
data = client_socket.recv(1024).decode('utf-8')
client_socket.close()

print(data)
