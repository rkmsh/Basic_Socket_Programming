#!/usr/bin/env python
#
# This program changes the mode to blocking or non-blocking
# We enable blocking by setting setblocking() to 1
# To disable it we will set setblocking() to 0

import socket

def test_socket_mode():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname()
    print "Trivial Server launched on socket: %s" %str(socket_address)

    while 1:
        s.listen(1)


if __name__ == "__main__":
    test_socket_mode()