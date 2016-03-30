import logging
import SocketServer

from .. network.server_handler import CrispyTCPServerHandler
from . connection import CrispyConnection

logger = logging.getLogger(__name__)

class CrispyTCPServer(SocketServer.TCPServer):
    """ Backend server methods for clients. """

    def __init__(self, server_address, handler_class=CrispyTCPServerHandler):
        self.allow_reuse_address = True
        self.clients = []
        self.current_id = 1
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return

    def add_session(self, conn):
        """ Add remote implant to clients list. """
	logger.debug("add_client() was called")
	#new_client = CrispyConnection({})
        # "Session {} opened ({}:{} <- {}:{})".format(self.current_id, server_ip, server_port, client_ip, client_port))
	self.clients.append(new_client)
    
    def remove_session(self, client):
        """ Remove remote implant from clients list. """
	logger.debug("remove_client() was called")
        self.clients.remove(client)
    
    def list_sessions(self):
        """ Return a list of sessions connected to the C2 server. """
	logger.debug("list_clients() was called")
        return self.clients
