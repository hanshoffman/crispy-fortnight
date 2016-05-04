import logging

from crispy.lib.module import *
from crispy.lib.fprint import *

logger = logging.getLogger(__name__)

__class_name__ = "DrivesModule"
class DrivesModule(CrispyModule):
    """ Enumerate the drives/mounts on a remote machine. """
    
    # can be: 'Darwin', 'Linux', 'Windows', 'Android'
    compatible_systems = ['Darwin']

    def marshall_darwin(self):
        import os

        partitions = os.listdir('/Volumes')
        
        info = ""
        for disk in partitions:
            info += "{}\n".format(disk)
        return info

    def run(self, args):
	logger.debug("run(args) was called")
        info("Getting partitions now...")
        
        if (self.is_compatible()):
            try:
                if self.client.is_darwin():
                    drives = self.client.conn.modules['os'].listdir('/Volumes')
                    for d in drives:
                        print "{}\n".format(d)
            except Exception as e:
                logger.error(e)
                error(e)
            
            success("Done.")
        else:
            error("Current OS's supported: {}".format(', '.join(self.compatible_systems)))
