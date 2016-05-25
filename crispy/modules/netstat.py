import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "NetstatModule"
class NetstatModule(CrispyModule):
    """ Display netstat info on a remote machine. """
    
    compatible_systems = ['Darwin', 'Linux']

    def run(self, args):
	logger.debug("run(args) was called")
       
        if (self.is_compatible()):
            if self.client.conn.modules['os'].geteuid() != 0:
                error("psutil requires this module to be run with root privileges")
                return
            else:
                spacing = "{:<10}{:<35}{:<35}{:<13}{:<6}{:<6}"
                print spacing.format("Protocol", "Local address", "Remote address", "Status", "PID", "Program name")
           
                AD = "-"
                #Protocol mapping: AF_UNIX = 1, AF_INET = 2, AF_INET6 = 10, kctl = 30 (for mac), SOCK_STREAM = 1, SOCK_DGRAM = 2
                proto_map = {(1, 1): 'tcp', (2, 1): 'tcp', (10, 1): 'tcp6', (1, 2): 'udp', (2, 2): 'udp', (10, 2): 'udp6', (30, 2): 'kctl'}
                proc_names = {}
                cpid = pid = self.client.conn.modules['os'].getpid()

                try:
                    for proc in self.client.conn.modules['psutil'].process_iter():    
                        proc_names[proc.pid] = proc.name()
                except KeyboardInterrupt:
                    logger.info("Caught Ctrl-C")
                except Exception as e:
                    pass
            
                try:
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
                except KeyboardInterrupt:
                    logger.info("Caught Ctrl-C")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
