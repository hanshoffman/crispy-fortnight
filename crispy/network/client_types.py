import socket

from abc import abstractmethod

class CrispyClientType(object):        
    @abstractmethod
    def connect(self, host, port):
        """Return a socket after a connection has occurred."""
        pass

class CrispyTCPClient(CrispyClientType):
    def __init__(self):
        self.family = socket.AF_INET
        self.protocol = socket.IPPROTO_TCP
        self.sock = None
        self.sock_type = socket.SOCK_STREAM
    
    def connect(self, host, port):
        family, socktype, proto, _, sockaddr = socket.getaddrinfo(host, port, self.family, self.sock_type, self.protocol)[0]
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        self.sock = s
        
        return s
