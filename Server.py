import socket


def my_server():
    # Start server
    try:
        server = socket.create_server(('127.0.0.1', 2000))
        server.listen(10)
        while True:
            HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html;' \
                   'charset=utf-8\r\n\r\n'
            # Waiting for a request
            print('Working...')
            client_socket, address = server.accept()
            # Processing request
            data = client_socket.recv(1024).decode('utf-8')
            content = (''.join(str.upper(data).split(' ')[1])
                       ).replace('/', '').replace('%20', ' ')

            # Answer
            client_socket.send(HDRS.encode('utf-8') + content.encode('utf-8'))
            # Client shutdown
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('shutdown...')


if __name__ == '__main__':
    my_server()
