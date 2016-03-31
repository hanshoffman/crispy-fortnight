import logging
import SocketServer

logger = logging.getLogger(__name__)

class CrispyTCPServerHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
	return
    
    def handle(self):
	logger.debug("connection from {}".format(self.client_address[0]))
        return
