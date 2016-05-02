import logging 
import socket

logger = logging.getLogger(__name__)

from abc import abstractmethod

class CrispyClient(object):        
    @abstractmethod
    def connect(self, host, port):
        """Return a socket after a connection has occurred."""
        pass

class TCPClient(CrispyClient):
    """ Client with no communication encryption. """

    def __init__(self, timeout=3, nodelay=False, keepalive=False):
        self.family = socket.AF_INET
        self.keepalive = keepalive
        self.nodelay = nodelay
        self.protocol = socket.IPPROTO_TCP
        self.sock = None
        self.sock_type = socket.SOCK_STREAM
        self.timeout = timeout

    def connect(self, host, port):
        family, socktype, proto, _, sockaddr = socket.getaddrinfo(host, port, self.family, self.sock_type, self.protocol)[0]
        s = socket.socket(family, socktype, proto)
        s.settimeout(self.timeout)
        s.connect(sockaddr)

        if self.nodelay:
            s.setsockopt(self.protocol, socket.TCP_NODELAY, 1)

        if self.keepalive:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

        self.sock = s
        return s

class SSLClient(TCPClient):
    """ Client with communication encryption. """
    
    def __init(self):
        pass

    def connect(self, host, port):
        pass
