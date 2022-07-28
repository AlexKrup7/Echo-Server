import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 2000))

# msg = input()
msg = "aaaaaa!"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()
