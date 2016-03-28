import logging
import SocketServer

logger = logging.getLogger(__name__)

class CrispyTCPServerHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
	return
    
    def setup(self):
        logger.debug("BaseRequestHandler: setup()")
        return SocketServer.BaseRequestHandler.setup(self)
    
    def handle(self):
	logger.debug("BaseRequestHandler: connection from {}".format(self.client_address))
        # "Session {} opened ({}:{} <- {}:{})".format(self.current_id, server_ip, server_port, client_ip, client_port))
        self.request.sendall("I am your master")
        return
    
    def finish(self):
        logger.debug("BaseRequestHandler: finish()")
        return SocketServer.BaseRequestHandler.finish(self) 
