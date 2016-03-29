import SocketServer

from crispy.network.server_handler import CrispyTCPServerHandler

class CrispyTCPServer(SocketServer.TCPServer):
    def __init__(self, server_address, handler_class=CrispyTCPServerHandler):
        self.allow_reuse_address = True
        self.clients = []
        self.current_id = 1
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return

    def add_client(self, conn):
        """Add remote implant to CrispyServer's sessions list"""
        self.clients.append(conn)
    
    def remove_client(self, client):
        """Remove remote implant from CrispyServer's sessions list"""
        self.clients.remove(client)
    
    def get_client_list(self):
        """Return a list of sessions connected to the CrispyServer"""
        return self.clients
