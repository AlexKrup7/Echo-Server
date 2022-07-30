import socket
from time import sleep

MAX_CONNECTIONS = 20
address_to_server = ('127.0.0.1', 8080)

clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in
           range(MAX_CONNECTIONS)]
for client in clients:
    client.connect(address_to_server)

for client in range(MAX_CONNECTIONS):
    msg = 'hi, how are u?'
    if clients[client].send(
            bytes("Message from client number " + str(client) + " - " + msg,
                  encoding='UTF-8')):
        print(clients[client].recv(1024).decode('utf-8').upper())
        sleep(3)
        clients[client].close()
