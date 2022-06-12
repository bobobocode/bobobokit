#!/usr/bin/env python3

import socket


def start(address, socket_handler):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ss.bind(address)
    ss.listen(2)
    while True:
        s, addr = ss.accept()
        print('Connection', addr)
        socket_handler(s)


def make_socket_handler(message_handler):

    def _handler(s):
        while True:
            request = s.recv(1024)
            if not request or b"\n" == request:
                break
            else:
                s.send(
                    message_handler(request.decode('utf-8'))
                    .encode('utf-8')
                )
        print('Closed')

    return _handler


def start_echo(address):

    def echo_handler(message):
        print(message)
        return message

    start(address, make_socket_handler(echo_handler))


if __name__ == "__main__":
    start_echo(('', 8080))
