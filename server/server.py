import socket

server = socket.socket()
server.bind(('', 2000))
server.listen(10)

while True:
    print('Working...')
    client_socket, address = server.accept()
    data = client_socket.recv(1024)
    if not data:
        break
    client_socket.send(data.upper())
    client_socket.close()
