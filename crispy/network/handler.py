import logging
import SocketServer

from .. lib.connection import CrispyConnection
from .. network.client_types import CrispyTCPClient

logger = logging.getLogger(__name__)

class CrispyTCPServerHandler(SocketServer.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
	return
    
    def handle(self):
	conn = CrispyConnection({"conn":self, "id":1, "user":"hdot", "platform":"darwin", "hostname":"GreenCouch.local", "macaddr":"60:f8:1d:b7:8e:b2"})
	self.server.add_session(conn)
	logger.debug(conn)
	return
