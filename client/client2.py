import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 2000))

msg = 'Asymptotic Analysis is the big idea that handles above issues in analyzing algorithms. In Asymptotic Analysis, we evaluate the performance of an algorithm in terms of input size (we don’t measure the actual running time). We calculate, how the time (or space) taken by an algorithm increases with the input size.'
client_socket.send(msg.encode())
data = client_socket.recv(1024).decode('utf-8')
client_socket.close()

print(data)
