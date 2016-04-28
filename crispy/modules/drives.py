import cPickle
import logging

from crispy.lib.myparser import CrispyArgumentParser
from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "DrivesModule"
class DrivesModule(CrispyModule):
    """ Enumerate the HDD's on a remote machine. """
    
    # can be: 'darwin', 'linux', 'windows', 'android'
    compatible_systems = ['darwin']

    def marshall_darwin(self):
        import os

        partitions = os.listdir('/Volumes')
        
        info = ""
        for disk in partitions:
            info += "{}\n".format(disk)
        return info

    def marshall_linux(self):
        pass

    def marshall_windows(self):
        pass

    def run(self, args):
	logger.debug("in DrivesModule run()")
        if (self.is_compatible()):
            try:
                if self.client.is_darwin():
	            info("Getting Disk Partitions in \"/Volumes\" now...\n")
                    data = cPickle.dumps(self.marshall_darwin(), -1)
                if self.client.is_linux():
                    pass
                if self.client.is_windows():
                    pass
                self.client.conn.sendall(data)
                print self.client.conn.recv(1024)
                success("Done.")
            except Exception as e:
                logger.error("{}: {}".format(__class_name__, e))
                error(e)
        else:
            error("OS not implmented yet... help me code it?")
