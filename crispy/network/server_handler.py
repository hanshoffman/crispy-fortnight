import logging
import SocketServer

module_logger = logging.getLogger('crispy_srv.CrispyTCPServerHandler')

class CrispyTCPServerHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
	self.logger = logging.getLogger('crispy_srv.CrispyTCPServerHandler')
	return
    
    def setup(self):
        self.debug("BaseRequestHandler: setup()")
        return SocketServer.BaseRequestHandler.setup(self)
    
    def handle(self):
        self.logger.debug("BaseRequestHandler: connection from {}".format(self.client_address))
        # "Session {} opened ({}:{} <- {}:{})".format(self.current_id, server_ip, server_port, client_ip, client_port))
        self.request.sendall("I am your master")
        return
    
    def finish(self):
        self.logger.debug("BaseRequestHandler: finish()")
        return SocketServer.BaseRequestHandler.finish(self) 
