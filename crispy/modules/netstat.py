import logging

from psutil import AccessDenied
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

#Protocol mapping
#AF_UNIX = 1, AF_INET = 2, AF_INET6 = 10, kctl = 30 (for mac)
#SOCK_STREAM = 1, SOCK_DGRAM = 2

__class_name__ = "NetstatModule"
class NetstatModule(CrispyModule):
    """ Display netstat info on a remote machine. """
    
    compatible_systems = ['Darwin', 'Linux']

    def run(self, args):
	logger.debug("run(args) was called")
       
        if (self.is_compatible()):
            spacing = "{:<10}{:<35}{:<35}{:<13}{:<6}{:<6}"
            print spacing.format("Protocol", "Local address", "Remote address", "Status", "PID", "Program name")
           
            AD = "-"
            proto_map = {(1, 1): 'tcp', (2, 1): 'tcp', (10, 1): 'tcp6', (1, 2): 'udp', (2, 2): 'udp', (10, 2): 'udp6', (30, 2): 'kctl'}
            proc_names = {}
            cpid = pid = self.client.conn.modules['os'].getpid()

            for proc in self.client.conn.modules['psutil'].process_iter():
                try:
                    proc_names[proc.pid] = proc.name()
                except AccessDenied: 
                    pass
            
            for c in self.client.conn.modules['psutil'].net_connections(kind='inet'):
                laddr, raddr = "", ""
                
                if c.laddr:
                    laddr = "{}:{}".format(c.laddr[0], c.laddr[1])
                if c.raddr:
                    raddr = "{}:{}".format(c.raddr[0], c.raddr[1])

                if c.pid == cpid:
                    highlight(spacing.format(proto_map[(c.family, c.type)], laddr or AD, raddr or AD, c.status or AD, c.pid or AD, proc_names.get(c.pid)), "yellow")
                else:
                    print spacing.format(proto_map[(c.family, c.type)], laddr or AD, raddr or AD, c.status or AD, c.pid or AD, proc_names.get(c.pid))
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
