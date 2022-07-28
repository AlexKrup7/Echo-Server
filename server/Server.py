import socket

sock = socket.socket()
sock.bind(('', 2000))
sock.listen(10)
conn, addr = sock.accept()

msg = ''

while True:
    data = conn.recv(1024)
    if not data:
        break
    msg += data.decode().upper()
    conn.send(data)

print(msg)

conn.close()
