import logging
import json
import SocketServer
import threading

logger = logging.getLogger(__name__)

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)

    def handle(self):
	tc = threading.current_thread()
	logger.debug("passing new threaded connection ({}) to server".format(tc.name))
	l = json.loads(self.request.recv(1024).strip())
        self.server.add_client(self, l)

    def finish(self):
	logger.debug("finish")
	#self.server.remove_client(self) #code works but need way to keep code in handle() until disconnects when finish() is then called	
