import logging 
import socket
import ssl

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
        super(TCPClient, self).__init__()
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
    
    def __init__(self, *args, **kwargs):
        self.ssl_kwargs = {"server_side" : False}
        
        if 'keyfile' in kwargs:
            self.ssl_kwargs["keyfile"] = kwargs['keyfile']
        
        if 'certfile' in kwargs:
            self.ssl_kwargs["certfile"] = kwargs['certfile']
        
        if 'ca_certs' in kwargs and kwargs['ca_certs'] is not None:
            self.ssl_kwargs["ca_certs"] = kwargs['ca_certs']
            self.ssl_kwargs["cert_reqs"] = ssl.CERT_REQUIRED
        
        if 'cert_reqs' in kwargs:
            self.ssl_kwargs["cert_reqs"] = kwargs['cert_reqs']
        
        if not 'ssl_version' in kwargs or kwargs['ssl_version'] is None:
            self.ssl_kwargs["ssl_version"] = ssl.PROTOCOL_TLSv1
        else:
            self.ssl_kwargs["ssl_version"] = kwargs['ssl_version']
        
        if 'ciphers' is kwargs:
            self.ssl_kwargs["ciphers"] = kwargs['cipher']
        
        super(SSLClient, self).__init__()

    def connect(self, host, port):
        s = super(SSLClient, self).connect(host, port)
        return ssl.wrap_socket(s, **self.ssl_kwargs)
