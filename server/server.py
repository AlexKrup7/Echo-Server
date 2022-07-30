import asyncio


class EchoServer(asyncio.Protocol):
    def connection_made(self, client):
        peername = client.get_extra_info('peername')
        print('connection from {}'.format(peername))
        self.client = client

    def data_received(self, data):
        print('data received: {}'.format(data.decode()))
        self.client.write(data)

        # close the socket
        self.client.close()


loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServer, '127.0.0.1', 8080)
server = loop.run_until_complete(coro)
print('serving on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    print("exit")
finally:
    server.close()
    loop.close()
