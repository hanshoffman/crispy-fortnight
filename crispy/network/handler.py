import logging
import SocketServer

from .. lib.client import CrispyClient

logger = logging.getLogger(__name__)

class CrispyTCPServerHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
    
    def handle(self):
	logger.debug("passing new connection to server")
	self.server.add_client(self)
	#need some way to stay in handle() until connection closes that way finish() can be called next to remove client once disconnected...
	
    def finish(self): #finish() is not what I need... it calls itself immediately after handle() which is obviously bad... what else?
	logger.debug("finish")
	#self.server.remove_client(self)
